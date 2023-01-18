from bs4 import BeautifulSoup
import os

def insert_to_xml_string(string, index, add_value):
    return string[:index] + add_value + '\n' + string[index:]

def insert_action(xml_file, add_intent):
    string_soup = str(xml_file)
    find_index = string_soup.find("/application>")-1
    if find_index != -1:
        after_change = insert_to_xml_string(string_soup, find_index,add_intent)
        xml_file = BeautifulSoup(after_change, 'xml')
        return xml_file
    else:
        return -1

def insert_intent(xml_file):
    add_intent = "<intent-filter> \n <action android:name=\"com.google.android.c2dm.intent.REGISTRATION\"/> \n </intent-filter>"
    xml_file = insert_action(xml_file,add_intent)
    add_intent = "<intent-filter> \n <action android:name=\"android.intent.action.AlertDialogs\"/> \n </intent-filter>"
    xml_file = insert_action(xml_file,add_intent)
    return xml_file


def insert_permission(xml_file):
    add_pre = "<uses-permission android:name=\"com.Aapp.UlagaTamilOli.permission.C2D_MESSAGE\"/>"
    string_soup = str(xml_file)
    find_index = string_soup.find("/manifest>")-1
    if find_index != -1:
        after_change = insert_to_xml_string(string_soup, find_index,add_pre)
        xml_file = BeautifulSoup(after_change, 'xml')
        return xml_file
    else:
        return -1

def insert_service(xml_file):
    add_pre = "<service android:name=\"com.arellomobile.android.push.PushGCMIntentService\"/>"
    string_soup = str(xml_file)
    find_index = string_soup.find("/application>")-1
    if find_index != -1:
        after_change = insert_to_xml_string(string_soup, find_index,add_pre)
        xml_file = BeautifulSoup(after_change, 'xml')
        return xml_file
    else:
        return -1
    
def save_manifest(path,xml_file):
    xml = open(path, "w")
    xml.write(xml_file.prettify())
    xml.close()

def change(path):
    path += "/AndroidManifest.xml"
    with open(path, 'r') as manifest:
        file = manifest.read() 
            # 'xml' is the parser used
    soup = BeautifulSoup(file, 'xml')
            # insert premission
    soup = insert_service(soup)
    if soup == -1:
        print("manifest -1", path)
        return
    soup = insert_intent(soup)
    if soup == -1:
        print("manifest -1", path)
        return
    soup = insert_permission(soup)
    if soup == -1:
        print("manifest -1", path)
        return
    save_manifest(path,soup)
    print("finish")
            # print(soup)



