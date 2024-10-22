import os
import argparse
import subprocess

def search_files(name1, name2):
    """
    Search for .blast, .gff, .len, .cds, and .pep files under the current directory based on the given names.
    :param name1: The first name
    :param name2: The second name
    :return: A dictionary containing the paths of the found files
    """
    current_dir = os.getcwd()  # Get the current working directory
    found_files = {}

    # Search for .blast file
    blast_file_name = f"{name1}_{name2}.blast"
    if os.path.exists(os.path.join(current_dir, blast_file_name)):
        found_files['blast'] = blast_file_name
    # Search for .gff files
    gff1_file_name = f"{name1}.gff"
    if os.path.exists(os.path.join(current_dir, gff1_file_name)):
        found_files['gff1'] = gff1_file_name
    gff2_file_name = f"{name2}.gff"
    if os.path.exists(os.path.join(current_dir, gff2_file_name)):
        found_files['gff2'] = gff2_file_name
    # Search for .len files
    len1_file_name = f"{name1}.len"
    if os.path.exists(os.path.join(current_dir, len1_file_name)):
        found_files['lens1'] = len1_file_name
    len2_file_name = f"{name2}.len"
    if os.path.exists(os.path.join(current_dir, len2_file_name)):
        found_files['lens2'] = len2_file_name
    # Search for .cds file, default is based on name1
    cds_file_name = f"{name1}_cds.fasta"
    if os.path.exists(os.path.join(current_dir, cds_file_name)):
        found_files['cds'] = cds_file_name
    # Search for .pep file, default is based on name1
    pep_file_name = f"{name1}_pep.fasta"
    if os.path.exists(os.path.join(current_dir, pep_file_name)):
        found_files['pep'] = pep_file_name
    return found_files

def create_dotplot_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory
    with the filename format {name1}_{name2}_dotplot.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_dotplot.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:
        file.write("[dotplot]\n")
        file.write(f"blast = {found_files.get('blast', '')}\n")
        file.write(f"gff1 = {found_files.get('gff1', '')}\n")
        file.write(f"gff2 = {found_files.get('gff2', '')}\n")
        file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        file.write(f"genome1_name = {name1}\n")
        file.write(f"genome2_name = {name2}\n")
        file.write("multiple = 1\n")
        file.write("score = 100\n")
        file.write("evalue = 1e-5\n")
        file.write("repeat_number = 10\n")
        file.write("position = order\n")
        file.write("blast_reverse = false\n")
        file.write("ancestor_left = none\n")
        file.write("ancestor_top = none\n")
        file.write("markersize = 0.5\n")
        file.write("figsize = 10,10\n")
        file.write(f"savefig = {name1}_{name2}_dotplot.pdf\n")
    
    print(f"File created: {file_name}")
    return file_name
def create_icl_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory
    with the filename format {name1}_{name2}_icl.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_icl.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:
        file.write("[collinearity]\n")
       
        file.write(f"gff1 = {found_files.get('gff1', '')}\n")
        file.write(f"gff2 = {found_files.get('gff2', '')}\n")
        file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        file.write(f"blast = {found_files.get('blast', '')}\n")
        file.write("blast_reverse = false\n")
        # file.write(f"genome1_name = {name1}\n")
        # file.write(f"genome2_name = {name2}\n")
        file.write("multiple = 1\n")
        file.write("process = 8\n")
        file.write("evalue = 1e-5\n")
        file.write("score = 100\n")
        file.write("grading = 50,40,25\n")
        file.write("mg=40,40\n")
        file.write("pvalue=0.2\n")
        file.write("repeat_number = 20\n")
        file.write("position = order\n")
        file.write(f"savefile = {name1}_{name2}_collinearity.txt\n")
    
    print(f"File created: {file_name}")
    return file_name
def create_ks_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_ks.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_ks.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:
        file.write("[ks]\n")
        file.write(f"cds_file = {found_files.get('cds', '')}\n")
        file.write(f"pep_file = {found_files.get('pep', '')}\n")
        file.write("align_software = muscle\n")
        file.write(f"pairs_file = {name1}_{name2}_collinearity.txt\n")
        file.write(f"ks_file = {name1}_ks_result.ks\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_blockinfo_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_blockinfo.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_blockinfo.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:
        file.write("[blockinfo]\n")
        file.write(f"blast = {found_files.get('blast', '')}\n")
        file.write(f"gff1 = {found_files.get('gff1', '')}\n")
        file.write(f"gff2 = {found_files.get('gff2', '')}\n")
        file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        file.write(f"collinearity = {name1}_{name2}_collinearity.txt\n")
        file.write("evalue = 1e-5\n")
        file.write("score = 100\n")
        file.write("repeat_number = 20\n")
        file.write("position = order\n")
        file.write(f"ks = {name1}_ks_result.ks\n")
        file.write(f"ks_col = ks_NG86\n")
        file.write(f"savefile = {name1}_{name2}_blockinfo.csv\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_blockks_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_blockks.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_blockks.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[blockks]\n")
        file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        file.write(f"genome1_name = {name1}\n")
        file.write(f"genome2_name = {name2}\n")
        file.write(f"blockinfo = {name1}_{name2}_blockinfo.csv\n")
        file.write("pvalue = 0.05\n")
        file.write("tandem = true\n")
        file.write("tandem_length = 200\n")
        file.write("makersize = 1\n")
        file.write("area = 0,3\n")
        file.write("block_length = 5\n")
        file.write("figsize = 8,8\n")
        file.write(f"savefig = {name1}_{name2}_blockks.pdf\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_kspeaks_conf_file(name1, name2, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_kspeaks.conf.
    :param name1: The first name
    :param name2: The second name
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_kspeaks.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[kspeaks]\n")
        file.write(f"blockinfo = {name1}_{name2}_blockinfo.csv\n")
        file.write("pvalue = 0.05\n")
        file.write("tandem = true\n") 
        file.write("block_length = 5\n")
        file.write("ks_area = 0,10\n")
        file.write("multiple = 1\n")
        file.write("homo = -1,1\n")
        file.write("fontsize = 9\n")
        file.write("area = 0,3\n")
        file.write("figsize = 10,6.18\n")
        
        file.write(f"savefig = {name1}_{name2}_kspeaks_distri.pdf\n")
        file.write(f"savefile = {name1}_{name2}_kspeaks_distri.csv\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_filtered_kspeaks_conf_file(name1, name2, ksarea_start, ksarea_end, peak_num, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}.conf.
    :param name1: The first name
    :param name2: The second name
    :param ksarea_start: The start value for the Ks area
    :param ksarea_end: The end value for the Ks area
    :param peak_num: The number of peaks (not used in the current implementation)
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[kspeaks]\n")
        file.write(f"blockinfo = {name1}_{name2}_blockinfo.csv\n")
        file.write("pvalue = 0.05\n")
        file.write("tandem = true\n") 
        file.write("block_length = 5\n")
        file.write(f"ks_area = {ksarea_start},{ksarea_end}\n")
        file.write("multiple = 1\n")
        file.write("homo = -1,1\n")
        file.write("fontsize = 9\n")
        file.write("area = 0,3\n")
        file.write("figsize = 10,6.18\n")
        file.write(f"savefig = {name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}_distri.pdf\n")
        file.write(f"savefile = {name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}_distri.csv\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_filtered_blockks_conf_file(name1, name2, ksarea_start, ksarea_end, peak_num, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_blockks_peaks_{peak_num}.conf.
    :param name1: The first name
    :param name2: The second name
    :param ksarea_start: The start value for the Ks area
    :param ksarea_end: The end value for the Ks area
    :param peak_num: The number of peaks
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_blockks_peaks_{peak_num}.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[blockks]\n")
        file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        file.write(f"genome1_name = {name1}\n")
        file.write(f"genome2_name = {name2}\n")
        file.write(f"blockinfo = {name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}_distri.csv\n")
        file.write("pvalue = 0.05\n")
        file.write("tandem = true\n")
        file.write("tandem_length = 200\n")
        file.write("makersize = 1\n")
        file.write("area = 0,3\n")
        file.write("block_length = 5\n")
        file.write("figsize = 8,8\n")
        file.write(f"savefig = {name1}_{name2}_blockks_peaks_{peak_num}.pdf\n")
    
    print(f"File created: {file_name}")
    return file_name
def create_peaksfit_conf_file(name1, name2, ksarea_start, ksarea_end, peak_num, found_files):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_peaksfit.conf.
    :param name1: The first name
    :param name2: The second name
    :param ksarea_start: The start value for the Ks area
    :param ksarea_end: The end value for the Ks area
    :param peak_num: The number of peaks
    :param found_files: A dictionary containing the paths of the found files
    """
    file_name = f"{name1}_{name2}_peaksfit.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[peaksfit]\n")
        file.write(f"blockinfo = {name1}_{name2}_kspeaks_{ksarea_start}_{ksarea_end}_distri.csv\n")
        file.write("mode = median\n")
        file.write("bins_number = 200\n")
        file.write("ks_area = 0,10\n")
        file.write("fontsize=9\n")
        file.write("area = 0,3\n")
        file.write("figsize = 10,6.18\n")
        file.write(f"savefig = {name1}_{name2}_peaksfit_{peak_num}.pdf\n")
    
    print(f"File created: {file_name}")
    return file_name

def create_ksfigure_data_conf_file(name1, name2, peak_num):
    """
    Create a configuration file in the current directory 
    with the filename format {name1}_{name2}_peaksfit.conf.
    :param name1: The first name
    :param name2: The second name
    :param peak_num: The number of peaks
    
    """
    file_name = f"{name1}_{name2}_ksfigure_data.csv"
    file_path = os.path.join(os.getcwd(), file_name)
     # 读取源文件的最后一行
    
    with open(file_path, 'w') as file: 
        # 动态生成 linestyle 后面的逗号
        extra_commas = ',' * (3 * peak_num)  
        file.write(f",color,linewidth,linestyle{extra_commas}\n")
        file.write(f"{name1}_{name2},green,1,-")
        file.close()
    for i in range(peak_num):
        source_file = f"peaksfit_{i+1}_result.txt"
        with open(source_file, 'r') as src_file:
            lines = src_file.readlines()
            last_line = lines[-1].strip() if lines else ""
            # 按 | 分割最后一行
            params = last_line.split('|')    
            # 写入提取的参数
            with open(file_path, 'a') as file:
                for param in params:
                    file.write(f",{param.strip()}")
    # 写入换行符
    with open(file_path, 'a') as file:
        file.write(f"\n")
    print(f"File created: {file_name}")
    return file_name
import os

def create_ksfigure_conf_file(name1, name2):
    """
    Create a configuration file in the current directory with the filename format {name1}_{name2}_ksfigure.conf.
    :param name1: First name
    :param name2: Second name
    :param found_files: Dictionary containing paths of found files
    """
    file_name = f"{name1}_{name2}_ksfigure.conf"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, 'w') as file:   
        file.write("[ksfigure]\n")
        # file.write(f"lens1 = {found_files.get('lens1', '')}\n")
        # file.write(f"lens2 = {found_files.get('lens2', '')}\n")
        # file.write(f"genome1_name = {name1}\n")
        # file.write(f"genome2_name = {name2}\n")
        file.write(f"ksfit = {name1}_{name2}_ksfigure_data.csv\n")
        file.write("labelfontsize = 15\n")
        file.write("legendfontsize = 15\n")
        file.write("xlabel = none\n")
        file.write("ylabel = none\n")
        file.write("title = none\n")

        file.write("area = 0,4\n")
        file.write("fontsize=9\n")

        # file.write("pvalue = 0.05\n")
        # file.write("tandem = true\n")
        # file.write("tandem_length = 200\n")
        # file.write("makersize = 1\n")
        # file.write("block_length = 5\n")
        file.write("figsize = 10,6.18\n")
        file.write("shadow = false\n")
        file.write(f"savefig = {name1}_{name2}_ksfigure.pdf\n")
    
    print(f"File created: {file_name}")
    return file_name

def run_wgdi_dotplot_command(conf_file):
    """
    Run the wgdi -d command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -d {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")
def run_wgdi_icl_command(conf_file):
    """
    Run the wgdi -icl command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -icl {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")
def run_wgdi_ks_command(conf_file):
    """
    Run the wgdi -ks command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -ks {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")

def run_wgdi_blockinfo_command(conf_file):
    """
    Run the wgdi -bi command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -bi {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")

def run_wgdi_blockks_command(conf_file):
    """
    Run the wgdi -bk command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -bk {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")
def run_wgdi_kspeaks_command(conf_file):
    """
    Run the wgdi -kp command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -kp {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")

def run_wgdi_filtered_kspeaks_command(conf_file):
    """
    Run the wgdi -kp command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -kp {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")
def run_wgdi_filtered_blockks_command(conf_file):
    """
    Run the wgdi -bk command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -bk {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")

def run_wgdi_peaksfit_command(conf_file, peaks_num):
    """
    Run the wgdi -pf command.
    :param conf_file: Path to the configuration file
    :param peaks_num: Number of peaks
    """
    command = f"wgdi -pf {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # Check if the command was executed successfully
    if result.returncode == 0:
        # Get the command output
        output = result.stdout
        print(output)
        # Define the output file path
        output_file = f"peaksfit_{peaks_num}_result.txt"
        # Write the output to a file
        with open(output_file, "w") as file:
            file.write(output)
        print(f"Results saved to {output_file}")
    else:
        print("Command execution failed")
        print(f"Error message: {result.stderr}")

def run_wgdi_ksfigure_command(conf_file):
    """
    Run the wgdi -kf command.
    :param conf_file: Path to the configuration file
    """
    command = f"wgdi -kf {conf_file}"
    print(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print(f"Error output: {e.stderr}")



def main():
    """
    Generate configuration files and run wgdi commands.
    """
    parser = argparse.ArgumentParser(description="Generate configuration files and run wgdi commands")
    parser.add_argument("name1", help="First species name")
    parser.add_argument("name2", help="Second species name")

    args = parser.parse_args()

    name1 = args.name1
    name2 = args.name2

    found_files = search_files(name1, name2)

    print(f"Found files:")
    for key, value in found_files.items():
        print(f"{key}: {value}")

    dotplot_conf_file = create_dotplot_conf_file(name1, name2, found_files)
    run_wgdi_dotplot_command(dotplot_conf_file)
    
    icl_conf_file = create_icl_conf_file(name1, name2, found_files)
    run_wgdi_icl_command(icl_conf_file)
    
    ks_conf_file = create_ks_conf_file(name1, name2, found_files)
    run_wgdi_ks_command(ks_conf_file)
    
    blockinfo_conf_file = create_blockinfo_conf_file(name1, name2, found_files)
    run_wgdi_blockinfo_command(blockinfo_conf_file)
    
    blockks_conf_file = create_blockks_conf_file(name1, name2, found_files)
    run_wgdi_blockks_command(blockks_conf_file)
    
    kspeaks_conf_file = create_kspeaks_conf_file(name1, name2, found_files)
    run_wgdi_kspeaks_command(kspeaks_conf_file)
    
    # Prompt user for peak_num and ksarea_start, ksarea_end
    peak_num = eval(input("Enter peak number: "))
    for i in range(peak_num):
        ksarea_start = eval(input("Enter peak start: "))
        ksarea_end = eval(input("Enter peak end: "))
        
        filtered_kspeaks_conf_file = create_filtered_kspeaks_conf_file(name1, name2, ksarea_start, ksarea_end, i + 1, found_files)
        run_wgdi_filtered_kspeaks_command(filtered_kspeaks_conf_file)
        
        filtered_blockks_conf_file = create_filtered_blockks_conf_file(name1, name2, ksarea_start, ksarea_end, i + 1, found_files)
        run_wgdi_filtered_blockks_command(filtered_blockks_conf_file)
        
        peaksfit_conf_file = create_peaksfit_conf_file(name1, name2, ksarea_start, ksarea_end, i + 1, found_files)
        run_wgdi_peaksfit_command(peaksfit_conf_file, i + 1)
        
        source_file = f"peaksfit_{i + 1}_result.txt"
    
    ksfigure_data_file = create_ksfigure_data_conf_file(name1, name2, peak_num)
    ksfigure_conf_file = create_ksfigure_conf_file(name1, name2)
    run_wgdi_ksfigure_command(ksfigure_conf_file)

if __name__ == "__main__":
    main()