import React, { Component } from "react";
import { Upload, Table, message, Typography } from "antd";
import axios from "axios";
import { DeleteTwoTone } from "@ant-design/icons";
import { Popconfirm, Button } from "antd";
import Layout from "../containers/NewLayout";

const bytesToSize = (bytes, decimals = 2) => {
  if (bytes === 0) return "0 Bytes";

  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

  const i = Math.floor(Math.log(bytes) / Math.log(k));

  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
};

const renderContent = (value, row, index) => {
  const obj = {
    children: value,
    props: {},
  };
  return obj;
};

class FileTable extends Component {
  state = {
    data: [],
  };
  
  confirm = (id) => {
    axios
      .delete("http://127.0.0.1:8000/api/delete", {
        data: {
          id: id,
        },
      })
      .then((res) => {
        message.info("File deleted successfully");
      });
  };

  columns = [
    {
      title: "Title",
      dataIndex: "uploaded_file_name",
      render: (value, row, index) => {
        const id = row["id"];
        return (
          <a
            onClick={() => {
              this.redirect(id);
            }}
          >
            {value}
          </a>
        );
      },
    },
    {
      title: "Uploaded On",
      dataIndex: "uploaded_on",
      render: renderContent,
      sorter: (a, b) => new Date(a.uploaded_on) - new Date(b.uploaded_on),
      sortDirections: ['descend', 'ascend'],
      showSorterTooltip:false 
    },
    {
      title: "Size",
      dataIndex: "size",
      render: bytesToSize,
    },
    {
      title: "Status",
      dataIndex: "status",
      render: renderContent,
    },
    {
      title: "Delete",
      dataIndex: "delete",
      render: (value, row, index) => {
        return (
          <Popconfirm
            placement="bottom"
            title={
              <div>
                Are you sure to delete this file ?<br></br> Your result will not
                be affected.
              </div>
            }
            onConfirm={() => {
              this.confirm(row["id"]);
            }}
            okText="Delete"
            cancelText="Cancel"
            okType="danger"
          >
            <DeleteTwoTone
              twoToneColor="#eb2f96"
              style={{ fontSize: "18px", cursor: "pointer" }}
            />
          </Popconfirm>
        );
      },
    },
  ];

  getList = () => {
    axios
      .get(
        "http://127.0.0.1:8000/api/get_file_list?username=" +
          localStorage.getItem("username")
      )
      .then((res) => {
        this.setState({
          data: res.data,
        });

        console.log(res.data);
      });
  };

  componentDidMount() {
    this.getList();
  }

  render() {

    return (
      <Layout selectedIndex="2" history={this.props.history}>
        <div
          style={{ paddingRight: "4%", paddingLeft: "4%", paddingTop: "50px" }}
        >
          <h2>Uploaded Files</h2>
          <Table dataSource={this.state.data} columns={this.columns}></Table>
        </div>
      </Layout>
    );
  }
}

export default FileTable;
