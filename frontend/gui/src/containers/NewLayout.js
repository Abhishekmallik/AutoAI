import React, { Component } from "react";
import { Layout } from "antd";
import { Menu, Dropdown } from "antd";
import classes from "./NewLayout.css";
import { Redirect } from "react-router-dom";
const { Header, Footer, Sider, Content } = Layout;

const menu = (
  <Menu>
    <Menu.Item key="1">Profile</Menu.Item>
    <Menu.Item key="2">Settings</Menu.Item>
    <Menu.Item key="3">Logout</Menu.Item>
  </Menu>
);
class CustomLayout extends Component {
  
  constructor(props){
    super(props);

  }
  
  state = {};
  handleVisibleChange = (flag) => {
    this.setState({ visible: flag });
  };

  

  render() {


  const redirect = (location) => {
     console.log(this.props.history.push(location))
     
  };
    return (
      <div class="root">
        <Layout>
          <Sider width="250" className={classes["sider"]}>
            <div className={classes["logo-container"]}>
              <img
                className={classes["logo"]}
                src="https://i.imgur.com/nsxu1O5.png"
              />
            </div>

            <Menu
              mode="inline"
              defaultSelectedKeys={this.props.selectedIndex}
              className={classes["menu"]}
            >
              <Menu.Item
                key="1"
                onClick={() => redirect("/home")}
                className={classes["menu-item"]}
              >
                Home
              </Menu.Item>
              <Menu.Item
                key="2"
                onClick={() => redirect("/files")}
                className={classes["menu-item"]}
              >
                Files
              </Menu.Item>
              <Menu.Item
                key="3"
                onClick={() => redirect("/result")}
                className={classes["menu-item"]}
              >
                Results
              </Menu.Item>
              <Menu.Item
                key="4"
                onClick={() => redirect("/home")}
                className={classes["menu-item"]}
              >
                Models
              </Menu.Item>
            </Menu>
          </Sider>

          <Layout className={classes["layout"]}>
            <Content className={classes["content-container"]}>
              <div className={classes["header"]}>
                <Dropdown overlay={menu} placement="bottomRight" arrow>
                  <img
                    className={classes["profile_photo"]}
                    src="https://qodebrisbane.com/wp-content/uploads/2019/07/This-is-not-a-person-2-1.jpeg"
                  ></img>
                </Dropdown>
              </div>
              {this.props.children}
            </Content>
          </Layout>
        </Layout>
      </div>
    );
  }
}

export default CustomLayout;

/*



<div
                  style={{
                    float: "right",
                    verticalAlign: "middle",
                    display: "table-cell",
                    borderLeft: "1px grey solid",
                    paddingLeft: "30px",
                  }}
                >
                   
                  <img
                    src="https://qodebrisbane.com/wp-content/uploads/2019/07/This-is-not-a-person-2-1.jpeg"
                    style={{ borderRadius: "50%", width: "50px" }}
                  ></img>
                    <Dropdown
                overlay={menu}
                onVisibleChange={this.handleVisibleChange}
                visible={this.state.visible}
              >
                  <span
                    style={{
                      paddingLeft: "6px",
                      fontSize: "16px",
                      fontFamily: "sans-serif",
                    }}
                  >

                    Aakash Kumar
                    
                  </span>
                  </Dropdown>
                </div>

                */
