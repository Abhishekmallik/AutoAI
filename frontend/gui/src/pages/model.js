import React, { Component } from "react";
import CustomLayout from "../containers/Layout";
import Form from "../containers/ModelForm";
import axios from "axios";
import { Card, Typography } from "antd";
const { Title } = Typography;
class Model extends Component {
  state = {
    dtypes: [],

  };
  componentDidMount() {
    let params = {
      id: sessionStorage.getItem("file_name"),
    };

    

    axios
      .get("http://127.0.0.1:8000/api/processedmetadata", { params: params })
      .then((res) => {
        this.setState({
          index: res.data["columns"],
        });
      });
  }

  render() {
    const heading = (title) => {
      return <Title style={{ fontWeight: "50" }}>{title}</Title>;
    };
    return (
      <div className="App">
        <CustomLayout k="4">
          <div>
            <Form data={this.state.index}></Form>
          </div>
          <p></p>
          <p></p>
        </CustomLayout>
      </div>
    );
  }
}
export default Model;
