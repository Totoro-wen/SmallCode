# -------------------------------------------------------------------------
# -*- coding:utf-8 -*-
# Author: Totoro
# function: 检查xml文件下是否存在object,将存在目标的xml文件和对应的图片拷贝到新的路径下
# -------------------------------------------------------------------------
import os
import csv
import shutil
import argparse
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description='xml and img')
    parser.add_argument('-m', '--org_img', default='/home/aibc/Desktop/person/pulic_data/all_img', help='original image path')
    parser.add_argument('-o', '--output_img', default='/home/aibc/Desktop/person/pulic_data/img', help='output image path')
    parser.add_argument('-x', '--org_xml', default='/home/aibc/Desktop/person/pulic_data/all_anno', help='all XML file paths')
    parser.add_argument('-l', '--output_xml', default='/home/aibc/Desktop/person/pulic_data/anno', help='output xml file path')
    args = parser.parse_args()
    return args

def main(args):
    # 判断输出目录是否存在,若不存在就创建
    if not os.path.exists(args.output_img):
        os.mkdir(args.output_img)
    if not os.path.exists(args.output_xml):
        os.mkdir(args.output_xml)
    # 判断xml文件内格式是否正确(是否存在Object)
    all_xml_path = args.org_xml
    for i in os.listdir(all_xml_path):
        path = all_xml_path + '/' + i
        tree = ET.parse(path)
        root = tree.getroot()
        # 判断xml文件里是否存在object
        if root.findall('object'):
            xml_file = path
            # 如果xml存在对应的标签person,将其拷贝到args.output_xml路径下
            shutil.copy(xml_file, args.output_xml)
            print('the xml file {0} is correct'.format(i))
        else:
            # # 如果xml不存在对应的标签person,将其对应的路径写入err_xml.csv
            f = open('err_xml.csv', 'w')
            writer = csv.writer(f)
            writer.writerow([path])
            print('--------------------------------no------------------------------------', path)

    # 判断每个xml文件是否都有对应的图片
    for j in os.listdir(args.output_xml):
        # 由xml文件生成对应图片的路径
        xml_name = j.split('.')[0]
        img_name = xml_name + '.jpg'
        file = args.org_img + '/' + img_name
        print('copy file {0}'.format(file))
        # 如果对应图片的路径存在,将其拷贝到args.output_img路径下
        if os.path.exists(file):
            shutil.copy(file, args.output_img)
        else:
            # 如果没有对应图片的路径,将其对应的路径写入err_img.csv
            f = open('err_img.csv', 'w')
            writer = csv.writer(f)
            writer.writerow([file])
            print('--------------------------------no------------------------------------', file)



if __name__ == '__main__':
    args = parse_arguments()
    main(args)





# 将xml文件对应的图片拷贝到新路径下img_path
# all_img = '/home/aibc/Desktop/VOC/org_img'
# xml_path = '/home/aibc/Desktop/VOC/Anno'
# img_path = '/home/aibc/Desktop/VOC/Data/'
# a = os.listdir(xml_path)[0].split('.')[0]
# for i in os.listdir(xml_path):
#     xml_name = i.split('.')[0]
#     img_name = xml_name + '.jpg'
#     file = all_img + '/' + img_name
#     shutil.copy(file, img_path)

# 将jpg文件对应的xml文件拷贝到新路径下anno
# all_img = '/home/aibc/Desktop/person/pulic_data/all_img'
# all_xml_path ='/home/aibc/Desktop/person/pulic_data/all_anno'
# img_path = '/home/aibc/Desktop/person/pulic_data/img'
# anno_path = '/home/aibc/Desktop/person/pulic_data/anno'
# # a = os.listdir(all_xml_path)[0].split('.')[0]
# for i in os.listdir(all_img):
#     # path = all_img + '/' + i
#     img_name = i.split('.')[0]
#     xml_name = img_name + '.xml'
#     file = all_xml_path + '/' + xml_name
#     if os.path.exists(file):
#         print('cope file ', file)
#         shutil.copy(file, anno_path)
#     else:
#         # 如果没有对应图片的路径,将其对应的路径写入err_img.csv
#         f = open('lack_xml.csv', 'w')
#         writer = csv.writer(f)
#         writer.writerow([file])
#         print('--------------------------------no------------------------------------', file)

# 判断xml文件是否存在object
# import xml.etree.ElementTree as ET
# tree = ET.parse('/home/aibc/Desktop/VOC/Anno/1_191.xml')
# root = tree.getroot()
# if root.findall('object'):
#     print(111)
# for event in root.findall('object'):
#     parties = event.find('name').text
#     if parties is None:
#         print("no")
#         continue
#     else:
#         print("true")