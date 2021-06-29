import React, { Component } from "react";
import { Form, Button, Select } from "antd";
import axios from "axios";
import { Card, Typography } from "antd";
import Table from "./AntTable";

const { Title } = Typography;
const { Option, OptGroup } = Select;
const { Meta } = Card;
const layout = {
  labelCol: { span: 4 },
  wrapperCol: { span: 10 },
};
const tailLayout = {
  wrapperCol: { offset: 4, span: 4 },
};

const index = [
  {
    title: "Date",
    dataIndex: "created_at",
    key: "date",
    render: (value, row, index) => {
      return (<p style={{fontSize:"15px"}}>{value}</p>);
    },
    sorter: (a, b) => new Date(a.created_at) - new Date(b.created_at),
    sortDirections: ['descend', 'ascend'],
    showSorterTooltip:false 
  },
  {
    title: "Model",
    dataIndex: "model",
    key: "model",
    render: (value, row, index) => {
      return (<p style={{fontSize:"15px"}}>{value}</p>);
    },
  },
  {
    title: "Parameters",
    dataIndex: "parameters",
    key: "parameters",
    render: (value, row, index) => {

      
      return (
        <div>
        {


              Object.entries(value).map(([metric,acc]) => {
                
                return  (<div>
                  <p style={{margin:'5px',fontSize:'15px'}}><span style={{color:"grey"}}>{metric}</span> : {String(acc)}</p>
                  </div>)
              })
        }
      </div>
      );
    },
  },
  {
    title: "Metrics",
    dataIndex: "metrics",
    key: "model",
    render: (value, row, index) => {

      return (
        <div>
          {
                Object.entries(value).map(([metric,acc]) => {
            
                  return  (<div>
                    <p style={{margin:'5px',fontSize:'15px'}}><span style={{color:"grey"}}>{metric}</span> : {JSON.stringify(acc)}</p>
                    </div>)
                })
          }
        </div>
      );
    },
  },
];

class Demo extends Component {
  formRef = React.createRef();

  state = {
    accuracy: "",
    visible: true,
    loading: false,
    results: [],
  };

  componentDidMount() {
    let params = {
      id: sessionStorage.getItem('file_name'),
      filter:"none"
    };


    const client = new WebSocket("ws://127.0.0.1:8000/result/?id="+params.id);
    client.onopen = (e) => {
      console.log("open", e);
    };
    client.onmessage = (e) => {
      console.log(e.data);
      if (e.data == "Result success") {
            getResult()
      }
    };
    client.onerror = (e) => {
      console.log("error", e);
    };



    const getResult = ()=>{

      axios
      .get("http://127.0.0.1:8000/api/results", { params: params })
      .then((res) => {
        this.setState({
          results: res.data,
          loading: false,
        });

      });
    }

    getResult();
      
  }

  

   onFinish = async(values) => {

    values['file_name'] = sessionStorage.getItem('file_name')
    axios.post('http://127.0.0.1:8000/api/result',JSON.stringify(values))
        .then(res=>{
        console.log(res)
        })
        
    }

  render() {
      const heading = (title) => {
        return <Title style={{ fontWeight: "50" }}>{title}</Title>;
      };

    const columns = this.props.data;
    if (columns == undefined) {
      return null;
    }

    let element = null;
    const createResult = () => {
      return (
        <div>
          <Table
            data={this.state.results}
            columns={index}
            bordered
            style={{ width: "100%" }}
          ></Table>
        </div>
      );
    };

    return (
      <div>
        <Card
          title={heading("Select Model")}
          bordered={false}
          style={{ width: "auto" }}
        >
          <Form
            {...layout}
            ref={this.formRef}
            name="control-ref"
            onFinish={this.onFinish}
            Post
          >
            <Form.Item
              name="target"
              label="Select Target Feature"
              rules={[{ required: true }]}
            >
              <Select
                showSearch
                placeholder="Select a option and change input text above"
                onChange={this.onGenderChange}
                allowClear
              >
                {columns.map((column) => {
                  return <Option value={column}>{column}</Option>;
                })}
              </Select>
            </Form.Item>

            <Form.Item name="model" label="Model" rules={[{ required: true }]}>
              <Select
                placeholder="Select a option and change input text above"
                onChange={this.onGenderChange}
                allowClear
              >
                 <OptGroup label="Classification">
                <Option value="decision_tree">Decision Tree</Option>
                <Option value="gaussian_naive_bayes">Gaussian Naive Bayes</Option>
                <Option value="knn">KNN</Option>
                <Option value="logistic_regression">Logistic Regression</Option>
                <Option value="random_forest">Random Forest</Option>
                <Option value="xgboost">XGBoost</Option>


                </OptGroup>

                <OptGroup label="Regression">
                <Option value="elsatic_net">ElasticNet</Option>
                <Option value="lasso_regression">Lasso Regression</Option>
                <Option value="linear_regression">Linear Regression</Option>
                <Option value="ridge_regression">Ridge Regression</Option>
                <Option value="sgd_regressor">SGD Regressor</Option>

                </OptGroup>
              </Select>
            </Form.Item>

            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
          </Form>
        </Card>

        <p></p>
        <Card
          title={heading("Result")}
          bodyStyle={{ padding: "0" }}
          bordered={false}
          style={{ width: "auto" }}
        >
          {createResult()}
        </Card>
      </div>
    );
  }
}

export default Demo;
