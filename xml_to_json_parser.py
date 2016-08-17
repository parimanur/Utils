import xml.etree.ElementTree as ET

class XmlToJsonParser:
    
    def ConvertXmlToJsonUtil(self,node,res):
        is_list = False
        if node.text and node.text.strip() not in ['', '\n', [], {}]:
            res[node.tag] = node.text
    
        elif node.tag in res:
            is_list = True
            #This condition is hit when 2nd element of list node is processed
            #Hence converting it to list 
            if type(res[node.tag])== dict:
                res[node.tag] = [res[node.tag]]
            #Empty dictionary is inserted for the resultant node to be filled using recursion
            res[node.tag].insert(0,{})
        
        else:
            res[node.tag] = {}
            
        for c in node.getchildren():
            
            if is_list:
                self.ConvertXmlToJsonUtil(c,res[node.tag][0])
            else:
                self.ConvertXmlToJsonUtil(c,res[node.tag])
    
        return res
    
    def ConvertXmlToJson(self,xml_string):
        
        xml_node_obj = ET.fromstring(xml_string)
        json_output = self.ConvertXmlToJsonUtil(xml_node_obj, {})
        return json_output