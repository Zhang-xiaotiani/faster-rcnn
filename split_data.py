import os


def main():
    # 定义Annotations文件夹路径
    annotations_path = "./CrowdHuman/Annotations/val"
    # 检查路径是否存在
    assert os.path.exists(annotations_path), f"Path '{annotations_path}' does not exist."

    # 获取所有.xml文件的文件名（不带扩展名）
    files_name = [file.split(".")[0] for file in os.listdir(annotations_path) if file.endswith(".xml")]
    # 对文件名进行排序
    files_name = sorted(files_name)

    # 定义输出文件路径
    output_path = "./CrowdHuman/ImageSets/val.txt"
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 将文件名写入train.txt文件
    try:
        with open(output_path, "w") as f:
            f.write("\n".join(files_name))
        print(f"File names have been successfully written to {output_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        exit(1)


if __name__ == '__main__':
    main()