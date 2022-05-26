import base64
import re
import subprocess
from pathlib import Path

import yaml

config_path = 'C:\coding\secret\kubeconfigs\oracle-cluster-config'
cert_path = 'C:\coding\secret\ssl'


def run_shell(c):
    p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()
    return out


def get_charts():
    values_yaml_paths = [x for x in Path().joinpath('../').resolve().glob('**/values.yaml')]
    values = []
    for path in values_yaml_paths:
        with open(path, "r") as stream:
            try:
                yaml_file = yaml.safe_load(stream)
                ingress_keys = [x for x in dict.keys(yaml_file) if 'ingress' in x or 'Ingress' in x]
                for key in ingress_keys:
                    if (yaml_file[key]['tls']) != 0:
                        for tls in yaml_file[key]['tls']:
                            values.append({
                                "path": path,
                                "yaml": yaml_file,
                                "host": tls["labels"]["tlsHost"].replace('wildcard', '*')
                            })
            except yaml.YAMLError:
                pass
    return values


def get_tls_secret():
    out = run_shell(f'kubectl --kubeconfig {config_path} get secrets -A --field-selector type=kubernetes.io/tls --show-labels')
    items = [re.sub(' +', ' ', x).split(' ') for x in out[0].decode('utf-8').split('\n')[1:-1]]
    secrets = []
    for item in items:
        try:
            secrets.append({
                "namespace": item[0],
                "name": item[1],
                "host": [x for x in item[-1].split(',') if 'tlsHost' in x][0].split('=')[1].replace('wildcard', '*')
            })
        except Exception:
            pass
    return secrets


def get_certs():
    hosts_paths = [x for x in Path(cert_path).glob('**/*') if x.is_dir()]
    hosts = []
    for hosts_path in hosts_paths:
        host = run_shell(f'certutil -dump {hosts_path.joinpath("fullchain.pem").absolute()}')[0].decode('utf-8').replace('\r\n', '\n').split('Subject:\n    CN=')[1].split('\n')[0]
        hosts.append({
            "path": hosts_path.absolute(),
            "name": hosts_path.name,
            "host": host
        })
    return hosts


if __name__ == '__main__':
    charts = get_charts()
    secrets = get_tls_secret()
    certs = get_certs()
    for cert in certs:
        crt = base64.b64encode(Path(cert["path"]).joinpath("fullchain.pem").open('r').read().encode('ascii')).decode('utf-8')
        key = base64.b64encode(Path(cert["path"]).joinpath("privkey.pem").open('r').read().encode('ascii')).decode('utf-8')
        for secret in secrets:
            if secret["host"] == cert["host"]:
                out = run_shell(f'kubectl --kubeconfig {config_path} get secrets -n {secret["namespace"]} {secret["name"]} -o=yaml')[0].decode('utf-8')
                yaml_file = yaml.safe_load(out)
                yaml_file["data"]["tls.crt"] = crt
                yaml_file["data"]["tls.key"] = key
                yy = yaml.safe_dump(yaml_file)
                o = open("./temp", "w")
                o.write(yy)
                o.close()
                run_shell(f'kubectl --kubeconfig {config_path} apply -f ./temp')
        for chart in charts:
            if chart["host"] == cert["host"]:
                with open(chart["path"], "r") as stream:
                    try:
                        yaml_file = yaml.safe_load(stream)
                        ingress_keys = [x for x in dict.keys(yaml_file) if 'ingress' in x or 'Ingress' in x]
                        for ingress in ingress_keys:
                            if (yaml_file[ingress]['tls']) != 0:
                                for tls in yaml_file[ingress]['tls']:
                                    tls["crt"] = crt
                                    tls["key"] = key
                        yy = yaml.safe_dump(yaml_file)
                        o = open(chart["path"], "w")
                        o.write(yy)
                        o.close()
                    except yaml.YAMLError:
                        pass
                with open(Path(chart["path"]).joinpath('../Chart.yaml').resolve().absolute(), "r") as stream:
                    try:
                        yaml_file = yaml.safe_load(stream)
                        vers = [int(x) for x in yaml_file["version"].split(".")]
                        vers[-1] = vers[-1] + 1
                        version = ".".join([str(x) for x in vers])
                        yaml_file["version"] = f"{version}"
                        yaml_file["appVersion"] = f'"{version}"'
                        yy = yaml.safe_dump(yaml_file)
                        o = open(Path(chart["path"]).joinpath('../Chart.yaml').resolve().absolute(), "w")
                        o.write(yy)
                        o.close()
                    except yaml.YAMLError:
                        pass
