import axios from "axios";
import React, { Component } from "react";
import CustomLayout from "../containers/Layout";

import { Affix, Button } from "antd";
import { Radio, Select } from "antd";
import Form from "../containers/PlotForm";
import { Card, Typography } from "antd";
import { Image } from 'antd';
import { Row, Col, Slider } from "antd";
const { Option } = Select;
const { Title } = Typography;

const heading = (title) => {
  return <Title style={{ fontWeight: "50" ,textAlign:"center"}}>{title}</Title>;
};
const params = {
  format: "json",
  id: sessionStorage.getItem("file_name"),
};




const tailFormItemLayout = {
  wrapperCol: {
    xs: {
      span: 24,
      offset: 0,
    },
    sm: {
      span: 16,
      offset: 8,
    },
  },
};
class Plots extends Component {
  state = {
    image_list: [],
    visible: false,
    original_columns :[],
    processed_columns :[]
  };

  componentDidMount() {



    let params = {
      id :sessionStorage.getItem('file_name')
    }



    axios
      .get("http://127.0.0.1:8000/api/processedmetadata", { params: params })
      .then((res) => {

       
        this.setState({
          processed_columns: res.data["columns"],
        });
        
      });

      axios.get('http://127.0.0.1:8000/api/csvmetadata',{params:params})
    .then(res=>{

      let columns = []

      res.data.map((value)=>{

        columns.push(value['index'])
      })
      


      this.setState({

        original_columns:columns
      })
      console.log(res.data)
    })
    

    
    const fetchData = ()=>{
    axios.get("http://127.0.0.1:8000/api/plot",{params:params}).then((response) => {
      this.setState({ image_list: response.data });
      console.log(response)
    });
  }
    var start = Date.now();
    this.setState({ source: "http://127.0.0.1:8000/static/temp.png" });
    var end = Date.now();
    console.log(end - start);


    const client = new WebSocket(
      "ws://127.0.0.1:8000/plot/?id=" + params.id
    );
    client.onopen = (e) => {
      console.log("open", e);
      const data = {
        id: sessionStorage.getItem("file_name"),
      };
      client.send(JSON.stringify(data));
    };
    client.onmessage = (e) => {
      console.log(e.data);
      if (e.data == "Success") {
        fetchData()
      }
    };
    client.onerror = (e) => {
      console.log("error", e);
    };
    
    fetchData()
  }

  render() {
    const Dstyle = {
      position: "fixed",
      right: "32px",
      bottom: "102px",
      zIndex: "2147483640",
      display: "-webkit-box",
      display: "-ms-flexbox",
      display: "flex",
    };

    const changeState = () => {
      this.setState({
        visible: true,
      });
    };

    const createLayout = () =>{


      const image_list = this.state.image_list ;
      console.log(this.state.image_list)
      let element =[];
      for(var key in image_list)
      {
        const e =(<Card 
        title={heading(key)}
        bordered={false}
        style={{ width: "auto",padding:'0px',marginBottom:'10px'}}
       
        bodyStyle={{ padding: "0"}}>
        {image_list[key].map((value)=>{
            console.log(value)
              return <Image  width={400} src={"http://127.0.0.1:8000/media/"+value['image_url']} alt={value['title']}></Image>
          })}
        </Card>   )
        element.push(e)
      }

      return element



    }



    
    return (
      <div className="App">
        <CustomLayout k="2">
          <Form visible={this.state.visible} processed_columns={this.state.processed_columns} original_columns={this.state.original_columns}></Form>

          

          <div style={Dstyle}>
            <img
              onClick={changeState}
              style={{ cursor: "pointer" }}
              src="https://www.flaticon.com/svg/vstatic/svg/1828/1828817.svg?token=exp=1612013571~hmac=448edff034979b00eb4d1b4f8d98ba0c"
              width="60px"
            ></img>
          </div>

          {createLayout(this.state.image_list)}
        </CustomLayout>
      </div>
    );
  }
}

export default Plots;
//<img src={this.state.source} />;


/*
<Card 
            title={heading("Histogram")}
            bordered={false}
            style={{ width: "auto",padding:'0px'}}
            
            bodyStyle={{ padding: "0"}}>
            <Row  gutter={[0, 0]} >
              <Col style={{borderRight:'1px solid grey',paddingTop:"10px", maxWidth:'100%',maxHeight:'100%'}}span={12} >
                <img src="http://127.0.0.1:8000/media/static/upload/random.png">
                </img>
            
                </Col>
                <Col style={{ paddingTop:"10px"}}span={12} >
                <img src="http://127.0.0.1:8000/media/static/upload/random.png">
                </img>
            
                </Col>
            </Row>
            <Row gutter={[0, 0]}>
            <Col style={{borderRight:'1px solid grey' ,borderTop:'1px solid grey',paddingTop:"10px"}}span={12} >
                <img src="http://127.0.0.1:8000/media/static/upload/random.png">
                </img>
            
                </Col>
                <Col style={{borderTop:'1px solid grey',paddingTop:"10px"}}span={12} >
                <img src="http://127.0.0.1:8000/media/static/upload/random.png">
                </img>
            
                </Col>
            </Row>
          </Card>

          */