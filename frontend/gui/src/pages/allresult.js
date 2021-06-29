import React, { Component } from "react";
import axios from "axios";
import Layout from "../containers/NewLayout";
import result from "./result";
import { Card, Typography } from "antd";
import Table from "../containers/AntTable";

const {Title} = Typography
const index = [
  {
    title: "Date",
    dataIndex: "created_at",
    key: "date",
    render: (value, row, index) => {
      return <p style={{ fontSize: "15px" }}>{value}</p>;
    },
  },
  {
    title: "Model",
    dataIndex: "model",
    key: "model",
    render: (value, row, index) => {
      return <p style={{ fontSize: "15px" }}>{value}</p>;
    },
  },
  {
    title: "Parameters",
    dataIndex: "parameters",
    key: "parameters",
    render: (value, row, index) => {
      return (
        <div>
          {Object.entries(value).map(([metric, acc]) => {
            return (
              <div>
                <p style={{ margin: "5px", fontSize: "15px" }}>
                  <span style={{ color: "grey" }}>{metric}</span> : {acc}
                </p>
              </div>
            );
          })}
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
          {Object.entries(value).map(([metric, acc]) => {
            return (
              <div>
                <p style={{ margin: "5px", fontSize: "15px" }}>
                  <span style={{ color: "grey" }}>{metric}</span> : {acc}
                </p>
              </div>
            );
          })}
        </div>
      );
    },
  },
];

class Result extends Component {
  state = {};

  componentDidMount() {
    let params = {
      id: "aakash",
      filter:"all"
      //sessionStorage.getItem("file_name"),
    };

    const getResult = () => {
      axios
        .get("http://127.0.0.1:8000/api/results", { params: params })
        .then((res) => {
          this.setState({
            results: res.data,
            loading: false,
          });
        });
    };

    getResult();
  }

  render() {
    const heading = (title) => {
      return <Title style={{ fontWeight: "50" }}>{title}</Title>;
    };

    const createResult = (accuracy) => {
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
      <Layout selectedIndex="3" history={this.props.history}>
          <div style={{ paddingRight: "4%", paddingLeft: "4%", paddingTop: "50px" }}>
          <h2>Results</h2>
          {createResult(95)}
       
        </div>
      </Layout>
    );
  }
}

export default Result;
