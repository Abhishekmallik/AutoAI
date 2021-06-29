import React, { useEffect, useState } from "react";
import { Button, Modal, Form, Input, Radio,Select } from 'antd';
import axios from 'axios'
const {Option}= Select

const formItemLayout = {
    labelCol: {
      xs: { span: 24 },
      sm: { span: 8 },
    },
    wrapperCol: {
      xs: { span: 24 },
      sm: { span: 16 },
    },
  };
const FormPlot = (props) => {
  const [form] = Form.useForm();
  const [visible,setVisible] = useState(false)
  const [columns,setColumns] = useState([])
 

  useEffect(()=>
  {
    setVisible(props.visible)

  },[props])

  const submitForm = (value)=>{

    console.log(value)
  }
  const onCreate = (values) => {
    console.log('Received values of form: ', values);
    
    
    values['id'] = sessionStorage.getItem('file_name')


    
    axios.post('http://127.0.0.1:8000/api/plot',JSON.stringify(values))
        .then(res=>{
        console.log(res)
        })

  };    

  const onChange = (value)=>{

    if(value=="original")
    {
      setColumns(props.original_columns)

    }

    if(value=="processed")
    {
      setColumns(props.processed_columns)

    }

  }
  
  return (
    <Modal
      visible={visible}
      title="Create a new plot"
      okText="Create"
      cancelText="Cancel"
      onCancel={()=>{
        setVisible(false)
      }
      }
      onOk={() => {
        form
          .validateFields()
          .then((values) => {
            form.resetFields();
            onCreate(values);
          })
          .catch((info) => {
            console.log('Validate Failed:', info);
          });
      }}
    >
      <Form
        form={form}
        {...formItemLayout}
        layout="horizontal"
        name="form_in_modal"
        initialValues={{
          modifier: "public",
        }}
      >
        <Form.Item
          name="title"
          label="Title"
          rules={[
            {
              required: true,
              message: "Please input the title of plot!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item name="dataset" label="Dataset">
          <Select showArrow onChange={onChange}>
            <Option value="original">Original</Option>
            <Option value="processed">Processed</Option>
          </Select>
        </Form.Item>

        <Form.Item name="type_of_plot" label="Plot Type">
          <Select>
            <Option value="scatter_plot">Scatter Plot</Option>
            <Option value="violin_plot">Violin Plot</Option>
            <Option value="bar_plot">Barplot</Option>
            <Option value="box_plot">Box Plot</Option>
            <Option value="sworm_plot">Sworm Plot</Option>

          </Select>
        </Form.Item>
        <Form.Item name="x_axis" label="Column (X-axis)">
          <Select  showArrow>
              {columns.map((values)=>{
               
                return <Option value={values}>{values}</Option>
              })}
          </Select>
        </Form.Item>

        <Form.Item name="x_axis_label" label="Label X">
          <Input type="textarea" />
        </Form.Item>

        <Form.Item name="y_axis" label="Column (Y-axis)">
          <Select>
          {columns.map((values)=>{
               
               return <Option value={values}>{values}</Option>
             })}
          </Select>
        </Form.Item>

        <Form.Item name="y_axis_label" label="Label Y">
          <Input type="textarea" />
        </Form.Item>
      </Form>
    </Modal>
  );


};

export default FormPlot;
