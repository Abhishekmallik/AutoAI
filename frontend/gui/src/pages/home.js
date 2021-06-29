import React,{Component} from 'react'
import CustomLayout from '../containers/Layout'
import { Card, Typography } from 'antd';
import { Upload, message } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import { Select } from 'antd';
import axios from 'axios'
import { Checkbox } from '@material-ui/core';
const { Option } = Select;



axios.defaults.withCredentials = true;

function onChange(value) {
  sessionStorage.setItem('file_name',value)
  
}


function onBlur() {
  console.log('blur');
}

function onFocus() {
  console.log('focus');
}

function onSearch(val) {
  console.log('search:', val);
}
const { Dragger } = Upload;



class Home extends Component{


    state = {
    
      files : []
    }


      getList = ()=>{
        axios.get('http://127.0.0.1:8000/api/get_file_list?username='+localStorage.getItem('username'))
        .then(res=>{
          this.setState({
            files:res.data
          })

          console.log(res.data)
        })

      }
    
      componentDidMount()
      {

        this.getList();
      
      }

      

    render(){

      
      const props = {
        name: 'file',
        multiple: false,
        action :'http://127.0.0.1:8000/api/upload_file?user='+localStorage.getItem('username'),
        onChange(info)  {
          const { status } = info.file;
      
          console.log(info.file)
          if (status !== 'uploading') {
            console.log(info.file, info.fileList);
          }
          if (status === 'done') {
            message.success(`${info.file.name} file uploaded successfully.`);

          } else if (status === 'error') {
            message.error(`${info.file.name} file upload failed.`);

          }
        },
      };
      

      function check(props)
      {
        props.history.push('/datasetinfo');
        
      }

       
        return (


    
        <div className="App">
          <CustomLayout  k="4">
            
          <Dragger {...props}>
            <p className="ant-upload-drag-icon">
            <InboxOutlined />
            </p>
            <p className="ant-upload-text">Click or drag file to this area to upload</p>
            <p className="ant-upload-hint">
            Support for a single or bulk upload. Strictly prohibit from uploading company data or other
            band files
            </p>
          </Dragger>

          <p></p>

          <Select
    showSearch
    style={{ width: 200 }}
    placeholder="Select a file"
    optionFilterProp="children"
    onChange={onChange}
    onFocus={onFocus}
    onBlur={onBlur}
    onSearch={onSearch}
  >

          

          
    
    
                {Object.values(this.state.files).map((file)=>{
                return <Option value={file['id']}>{file['uploaded_file_name']}</Option>
                })}

                
    
      </Select>
          </CustomLayout>
        <button onClick={()=>check(this.props)}>
                Go
        </button> 
        
        </div>
      );
    }
}
export default  Home; 