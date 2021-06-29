import React, { Component } from "react";
import { Table } from "antd";

const rowGenrator = (list) => {
  let columns = [];
  for (let i = 0; i < list.length; i++) {
    columns.push({
      title: list[i],
      dataIndex: list[i],
      key: list[i],
      render:(value,row,index)=>{

        return (<div>{JSON.stringify(value)}</div>)
      }
    });
  }
  return columns;
};



class TableNew extends Component {
  state = {};
  

  render() {

    return (
      <div>
        <Table
          columns={this.props.columns}
          dataSource={this.props.data}
          pagination={false}
          bordered
        />
      </div>
    );
  }
}

export default TableNew;
