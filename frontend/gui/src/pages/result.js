import React, { Component } from "react";
import axios from "axios";
import { Collapse, Space } from "antd";
import CustomLayout from "../containers/Layout";
import { Card, Typography } from "antd";
import { Row, Col, Slider } from "antd";
const { Title } = Typography;
const { Panel } = Collapse;

const heading = (title) => {
  return <Title style={{ fontWeight: "50" }}>{title}</Title>;
};

function callback(key) {
  console.log(key);
}

class Result extends Component {
  state = {};

  componentDidMount() {}

  render() {
    return (
      <CustomLayout>
        <Card
          title={heading("Result")}
          bordered={false}
          style={{ width: "auto" }}
        >
          <Row gutter={[16, 8]}>
            <Col span={8}>
              <p style={{ fontSize: "15px" }}>
                <span style={{ color: "grey", paddingRight: "4px" }}>
                  Date :
                </span>{" "}
                26-01-2021 18:30{" "}
              </p>
            </Col>
            <Col span={8}>
              <p style={{ fontSize: "15px" }}>
                <span style={{ color: "grey", paddingRight: "4px" }}>
                  Model :
                </span>{" "}
                Logistic Regression{" "}
              </p>
            </Col>

            <Col span={8}>
              <p style={{ fontSize: "15px" }}>
                <span style={{ color: "grey", paddingRight: "4px" }}>
                  Time Taken :{" "}
                </span>
                32 second{" "}
              </p>
            </Col>
          </Row>
          <Row gutter={[16, 8]}>
            <Col span={8} />
            <Col span={8} />
            <Col span={8} />
          </Row>
          <Collapse defaultActiveKey={["1"]} ghost>
            <Panel header="Metrics" key="1">
              <table>
                <tbody>
                  <tr
                    style={{
                      borderTop: "1px solid grey",
                      borderBottom: "1px solid grey",
                      fontSize: "15px",
                    }}
                  >
                    <td style={{ paddingRight: "25px" }}>accuracy</td>
                    <td>0.6343283582089553</td>
                  </tr>
                  <tr
                    style={{
                      borderTop: "1px solid grey",
                      borderBottom: "1px solid grey",
                      fontSize: "15px",
                    }}
                  >
                    <td style={{ paddingRight: "25px" }}>f1-score</td>
                    <td>0.1090909090909091</td>
                  </tr>
                </tbody>
              </table>
            </Panel>
            <Panel header="Parameters" key="2">
              <table>
                <tbody>
                  <tr
                    style={{
                      borderTop: "1px solid grey",
                      borderBottom: "1px solid grey",
                      fontSize: "15px",
                    }}
                  >
                    <td style={{ paddingRight: "25px" }}>accuracy</td>
                    <td>0.6343283582089553</td>
                  </tr>
                  <tr
                    style={{
                      borderTop: "1px solid grey",
                      borderBottom: "1px solid grey",
                      fontSize: "15px",
                    }}
                  >
                    <td style={{ paddingRight: "25px" }}>f1-score</td>
                    <td>0.1090909090909091</td>
                  </tr>
                </tbody>
              </table>
            </Panel>
            <Panel header="Confusion Matrix" key="3">
              <img src="data:image/png;base64,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"></img>
            </Panel>
          </Collapse>
        </Card>
      </CustomLayout>
    );
  }
}

export default Result;
