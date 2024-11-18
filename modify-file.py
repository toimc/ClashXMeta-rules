import yaml
import os

# 解析输入数据并生成YAML格式
def convert_to_yaml(input_data):
    payload = []
    for line in input_data.strip().splitlines():
        # 分割规则类型和具体内容
        parts = line.split(",", 2)
        if len(parts) < 2:
            print(f"Skipping line due to insufficient data: {line}")
            continue
        rule_type, rule_value = parts[0], parts[1]
        payload.append(f"{rule_type},{rule_value}")
    
    # 构造YAML数据结构
    output_data = {"payload": payload}
    
    # 输出YAML格式
    return yaml.dump(output_data, sort_keys=False, default_flow_style=False)

# 创建output目录
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 读取Input目录下的所有文件
input_dir = "Input"
for filename in os.listdir(input_dir):
    if not filename.endswith(".txt"):
        print(f"Skipping non-txt file: {filename}")
        continue
    input_file_path = os.path.join(input_dir, filename)
    
    # 读取文件内容
    with open(input_file_path, "r") as infile:
        input_data = infile.read()
    
    # 转换数据
    output_yaml = convert_to_yaml(input_data)
    
    # 保存到output目录，文件名与输入文件名相同，后缀为.yaml
    output_file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.yaml")
    with open(output_file_path, "w") as outfile:
        outfile.write(output_yaml)

    print(f"Processed {filename} and saved to {output_file_path}")