import React, { Component } from "react";
import { connect } from "react-redux";
import * as actions from "../store/actions/auth";
import { Form } from "antd";
import classes from "./login.css";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";

class Login extends Component {
  state = {
    open: false,
    isAuthenticated:false,
  };

  handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }
    this.setState({ open: false });
  };


  componentDidMount(){
    this.props.onTryAutoSignup();
  }

  render() {
    const onFinish = (values) => {

      this.props.onAuth(values.username, values.password).then(() => {
        const token = localStorage.getItem("token");

        if (token !== null) {

          // Authenticated
          this.state.isAuthenticated = true;
          this.props.history.push('/home')

        } else {
          
          //Incorrect username or password
          this.setState({ open: true });
        }
      });
    };

    const onFinishFailed = (errorInfo) => {};

    if(localStorage.getItem('token')!=null)
    {
      this.props.history.push('/home')
    }


    return (
      <div>
        <div className={classes["back"]}>
          <div className={classes["div-center"]}>
            <div className={classes["content"]}>
              <h1 className={classes["title"]}>Welcome</h1>
              <div style={{ textAlign: "center" }}>
                <img
                  className={classes["login_logo"]}
                  src="https://i.imgur.com/nsxu1O5.png"
                  width="70"
                />
              </div>

              <Snackbar
                anchorOrigin={{ vertical: "top", horizontal: "center" }}
                open={this.state.open}
                autoHideDuration={6000}
                onClose={this.handleClose}
              >
                <MuiAlert onClose={this.handleClose} severity="error">
                  Incorrect username or password
                </MuiAlert>
              </Snackbar>
              <Form
                layout="vertical"
                name="basic"
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
              >
                <Form.Item
                  name="username"
                  rules={[
                    {
                      required: true,
                      message: "Please input your username!",
                    },
                  ]}
                >
                  <TextField
                    style={{ width: "100%" }}
                    size="medium"
                    label="Username"
                  />
                </Form.Item>

                <Form.Item
                  name="password"
                  rules={[
                    {
                      required: true,
                      message: "Please input your password!",
                    },
                  ]}
                >
                  <TextField
                    style={{ width: "100%" }}
                    label="Password"
                    type="password"
                  />
                </Form.Item>

                <Form.Item style={{ marginTop: "50px" }}>
                  <Button
                    className={classes["btn"]}
                    variant="outlined"
                    type="submit"
                  >
                    Login
                  </Button>
                </Form.Item>
              </Form>
              <p className={classes['signup_label']}>
                Don’t have an account?  
                <a src="#">
                Sign Up
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onAuth: (username, password) =>
      dispatch(actions.authLogin(username, password)),

      onTryAutoSignup :() =>dispatch(actions.authCheckState())
  };
};

const mapStateToProps = (state) => {
  return {
    loading: state.loading,
    error: state.error,
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Login);
