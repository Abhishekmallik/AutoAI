import React, { Component } from "react";
import CustomLayout from "../containers/NewLayout";
import { Upload, Table, message, Typography } from "antd";
import axios from "axios";
import { Redirect } from "react-router-dom";
const { Dragger } = Upload;

const uploadContainer = {
  minHeight: "330px",
  padding: "50px 20% 0 20%",
  height: "auto",
};

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



class Home extends Component {
  
  
  redirect = (id) => {
    console.log(id)
    sessionStorage.setItem("file_name", id);
    this.props.history.push('/datasetinfo')
  };
  
  
  columns = [
    {
      title: "Title",
      dataIndex: "uploaded_file_name",
      render: (value, row, index) => {
        const id = row['id']
        return <a onClick={()=>{this.redirect(id)}}>{value}</a>;
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
  ];

  state = {
    data: [],
  };

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

  uploadFile = (info) => {
    const { status } = info.file;

    console.log(info.file);
    if (status !== "uploading") {
      console.log(info.file, info.fileList);
    }
    if (status === "done") {
      message.success(`${info.file.name} file uploaded successfully.`);
      this.getList();
    } else if (status === "error") {
      message.error(`${info.file.name} file upload failed.`);
    }
  };

  deleteFile = (info) => {};

  componentDidMount() {
    this.getList();
  }

  render() {
    const props = {
      name: "file",
      multiple: false,
      action:
        "http://127.0.0.1:8000/api/upload_file?user=" +
        localStorage.getItem("username"),
      showUploadList: true,
      precision: 2,
      progress: {
        type: "line",
        format: (percent) => {
          return (Math.round(percent * 100) / 100).toFixed(1) + "%";
        },
        style: { width: "100%" },
      },
    };

    return (
      <div className="root">
        <CustomLayout selectedIndex="1" history={this.props.history}>
          <div style={uploadContainer}>
            <Dragger {...props} onChange={this.uploadFile}>
              <p className="ant-upload-drag-icon">
                <img
                  src="https://cdn1.iconfinder.com/data/icons/hawcons/32/698394-icon-130-cloud-upload-512.png"
                  width="100px"
                ></img>
              </p>
              <p className="ant-upload-text">
                Click or drag file to this area to upload
              </p>
              <p className="ant-upload-hint">Only CSV Files are allowed</p>
            </Dragger>
          </div>

          <div>
            <div style={{ paddingRight: "4%", paddingLeft: "4%" }}>
              <h2>Recently Uploaded Files</h2>
              <Table
                columns={this.columns}
                dataSource={this.state.data}
                pagination={{ pageSize: 5 }}
                bordered
              />
            </div>
          </div>
        </CustomLayout>
      </div>
    );
  }
}

export default Home;
