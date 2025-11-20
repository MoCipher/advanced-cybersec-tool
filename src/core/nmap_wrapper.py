class NmapWrapper:
    def __init__(self, nmap_path='nmap'):
        self.nmap_path = nmap_path

    def run_nmap_scan(self, target, options=''):
        import subprocess
        command = [self.nmap_path] + options.split() + [target]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running Nmap scan: {e}")
            return None

    def parse_nmap_output(self, nmap_output):
        import xml.etree.ElementTree as ET
        try:
            root = ET.fromstring(nmap_output)
            hosts = []
            for host in root.findall('host'):
                host_info = {
                    'address': host.find('address').get('addr'),
                    'hostname': host.find('hostnames/hostname').get('name') if host.find('hostnames/hostname') is not None else None,
                    'ports': []
                }
                for port in host.findall('ports/port'):
                    port_info = {
                        'port_id': port.get('portid'),
                        'protocol': port.get('protocol'),
                        'state': port.find('state').get('state')
                    }
                    host_info['ports'].append(port_info)
                hosts.append(host_info)
            return hosts
        except ET.ParseError as e:
            print(f"Error parsing Nmap output: {e}")
            return None