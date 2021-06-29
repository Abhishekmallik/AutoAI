import axios from "axios";
import React, { Component } from "react";
import CustomLayout from "../containers/Layout";
import Table from "../containers/Table";
import VerticalTable from "../containers/VerticalTable";
import { Spin } from "antd";
import { LoadingOutlined } from "@ant-design/icons";

const antIcon = <LoadingOutlined style={{ fontSize: 100 }} spin />;

class DatasetInfo extends Component {
  state = {
    head: [],
    describe: {},
    missing: {},
    loading: true,
  };
  componentDidMount() {
    const params = {
      format: "json",
      id: sessionStorage.getItem("file_name"),
    };

    const fetchData = () => {
      axios
        .get("http://127.0.0.1:8000/api/dataset", { params: params })
        .then((res) => {
          this.setState({
            head: res.data["head"],
            describe: res.data["describe"],
            missing: res.data["missing"],
          });

          if (
            Object.keys(res.data).length !== 0 &&
            res.data.constructor === Object
          ) {
            this.setState({
              loading: false,
            });
          }
        });
    };

    fetchData();

    if (this.state.loading === true) {
      const client = new WebSocket(
        "ws://127.0.0.1:8000/dataset?id=" + params.id
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
          fetchData();
        }
      };
      client.onerror = (e) => {
        console.log("error", e);
      };
    }
  }
  render() {
    return (
      <div className="App">
        <CustomLayout k="1">
          {this.state.loading ? (
            <div
              style={{
                textAlign: "center",
                height: "100%",
                display: "table",
                width: "100%",
              }}
            >
              <Spin
                style={{ verticalAlign: "middle", display: "table-cell" }}
                indicator={antIcon}
              ></Spin>
            </div>
          ) : (
            <div>
              <Table title="Head" data={this.state.head}>
                Head
              </Table>
              <VerticalTable
                title="Describe"
                data={this.state.describe}
              ></VerticalTable>
              <VerticalTable
                title="Missing"
                data={this.state.missing}
              ></VerticalTable>
            </div>
          )}
        </CustomLayout>
      </div>
    );
  }
}

export default DatasetInfo;