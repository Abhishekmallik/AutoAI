import React, { useState, useRef, useEffect } from "react";
import PropTypes from "prop-types";
import clsx from "clsx";
import { lighten, makeStyles, createMuiTheme } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import Checkbox from "@material-ui/core/Checkbox";
import { Menu, Dropdown, message, Button } from "antd";
import { DownOutlined } from "@ant-design/icons";
import { Tag, Select } from "antd";
import axios from "axios";

const { Option, OptGroup } = Select;
const headCells = [
  { id: "index", numeric: false, disablePadding: true, label: "Column" },
  { id: "dtypes", numeric: false, disablePadding: false, label: "Data Type" },
  {
    id: "total_missing",
    numeric: false,
    disablePadding: false,
    label: "Total Missing",
  },
  { id: "encoder", numeric: false, disablePadding: false, label: "Encoder" },
  {
    id: "normalizer",
    numeric: false,
    disablePadding: false,
    label: "Normalizer",
  },
];

function EnhancedTableHead(props) {
  const { onSelectAllClick, numSelected, rowCount } = props;

  return (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox">
          <Checkbox
            indeterminate={numSelected > 0 && numSelected < rowCount}
            checked={rowCount > 0 && numSelected === rowCount}
            onChange={onSelectAllClick}
            inputProps={{ "aria-label": "Select all columns" }}
          />
        </TableCell>

        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            align={"left"}
            padding={headCell.disablePadding ? "none" : "default"}
          >
            {headCell.label}
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}


EnhancedTableHead.propTypes = {
  classes: PropTypes.object.isRequired,
  numSelected: PropTypes.number.isRequired,
  onSelectAllClick: PropTypes.func.isRequired,
  rowCount: PropTypes.number.isRequired,
};

const useToolbarStyles = makeStyles((theme) => ({
  root: {
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(1),
  },
  highlight:
    theme.palette.type === "light"
      ? {
          color: theme.palette.secondary.main,
          backgroundColor: lighten(theme.palette.secondary.light, 0.85),
        }
      : {
          color: theme.palette.text.primary,
          backgroundColor: theme.palette.secondary.dark,
        },
  title: {
    flex: "1 1 100%",
  },
}));

const EnhancedTableToolbar = (props) => {
  const classes = useToolbarStyles();
  const { numSelected } = props;

  return (
    <Toolbar className={clsx(classes.root, {})}>
      {
        <Typography
          className={classes.title}
          variant="h6"
          id="tableTitle"
          component="div"
        >
          Process Dataset
        </Typography>
      }
    </Toolbar>
  );
};

EnhancedTableToolbar.propTypes = {
  numSelected: PropTypes.number.isRequired,
};

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  paper: {
    width: "100%",
    marginBottom: theme.spacing(2),
  },
  table: {
    minWidth: 750,
  },
  visuallyHidden: {
    border: 0,
    clip: "rect(0 0 0 0)",
    height: 1,
    margin: -1,
    overflow: "hidden",
    padding: 0,
    position: "absolute",
    top: 20,
    width: 1,
  },

  table: {
    "& Mui-selected:": {
      color: "red",
      backgroundColor: "red",
    },
  },
}));

export default function EnhancedTable(props) {
  const classes = useStyles();
  const [selected, setSelected] = React.useState(props.columns);
  const [action, setAction] = React.useState({});
  const [encoder, setEncoder] = React.useState({});
  const [normalizer, setNormalizer] = React.useState({});



    useEffect(() => {
     
      if(props.normalizer)
      {
        setNormalizer(props.normalizer)
      }
      if(props.encoder)
      {
        setEncoder(props.encoder)
      }
      
      if(props.actions)
      {
        setAction(props.actions)
      }
      if(props.columns)
      {
        setSelected(props.columns)
      }
   }, [props])

 




  const handleSelectAllClick = (event) => {
    if (event.target.checked) {
      const newSelecteds = props.data.map((n) => n.index);
      setSelected(newSelecteds);
      return;
    }
    setSelected([]);
  };

  const handleClick = (event, name) => {
    if (String(event.target) !== "[object HTMLInputElement]") {
      return;
    }
    const selectedIndex = selected.indexOf(name);
    let newSelected = [];

    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, name);
    } else if (selectedIndex === 0) {
      newSelected = newSelected.concat(selected.slice(1));
    } else if (selectedIndex === selected.length - 1) {
      newSelected = newSelected.concat(selected.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelected = newSelected.concat(
        selected.slice(0, selectedIndex),
        selected.slice(selectedIndex + 1)
      );
    }
    setSelected(newSelected);
  };

  const isSelected = (name) => selected.indexOf(name) !== -1;

  const data = props.data;

  if (Object.keys(data).length === 0) {
    return null;
  }

  const handleMenuClick = (e) => {
    let obj = e.key;
    obj = JSON.parse(obj);
    let pre = { ...action };
    pre[obj.column] = obj["action"];
    setAction(pre);

    console.log(action);
  };

  const handleEncoderChange = (value, columnName) => {
    let newEncoder = { ...encoder };
    newEncoder[columnName] = value;
    setEncoder(newEncoder);
  };

  const handelNormalizerChange = (value, columnName) => {
    let newNormalizer = { ...normalizer };
    newNormalizer[columnName] = value;
    setNormalizer(newNormalizer);
  };

  const generateTag = (color, message) => {
    return (
      <Tag color={color} style={{ marginLeft: "7px" }}>
        {message}
      </Tag>
    );
  };

  const genrateKey = (index, colName, action) => {
    return `{ "id": "${index}",
          "column": "${colName}",
          "action": "${action}"}`;
  };

  const labels = (name) => {
    let c = action[name];

    switch (c) {
      case "mean":
        return generateTag("success", "Replaced with mean");

      case "median":
        return generateTag("success", "Replaced with median");

      case "mode":
        return generateTag("success", "Replaced with mode");

      case "delete_missing":
        return generateTag("error", "Delete Missing Records");

      case "delete_column":
        return generateTag("error", "Delete Column");

      case "rep_min_freq":
        return generateTag("success", "Replace with minimum frequency");

      case "rep_max_freq":
        return generateTag("success", "Replace with maximum frequency");
    }
  };

  const menu1 = (index, colName) => {
    return (
      <Menu onClick={handleMenuClick}>
        <Menu.Item key={genrateKey(index, colName, "mean")}>
          Replace with mean
        </Menu.Item>
        <Menu.Item key={genrateKey(index, colName, "median")}>
          Replace with median
        </Menu.Item>
        <Menu.Item key={genrateKey(index, colName, "mode")}>
          Replace with mode
        </Menu.Item>
        <Menu.Item danger key={genrateKey(index, colName, "delete_missing")}>
          Delete Missing Records
        </Menu.Item>
        <Menu.Item danger key={genrateKey(index, colName, "delete_column")}>
          Delete Column
        </Menu.Item>
      </Menu>
    );
  };

  const menu2 = (index, colName) => {
    return (
      <Menu onClick={handleMenuClick}>
        <Menu.Item key={genrateKey(index, colName, "rep_min_freq")}>
          Replace with minimum frequency
        </Menu.Item>
        <Menu.Item key={genrateKey(index, colName, "rep_max_freq")}>
          Replace with maximum frequency
        </Menu.Item>
        <Menu.Item danger key={genrateKey(index, colName, "delete_missing")}>
          Delete Missing Records
        </Menu.Item>
        <Menu.Item danger key={genrateKey(index, colName, "delete_column")}>
          Delete Column
        </Menu.Item>
      </Menu>
    );
  };

  let rowData = [];

  const dtypes = ["int64", "float64", "decimal"];

  for (var i = 0; i < data.length; i++) {
    const isItemSelected = isSelected(data[i]["index"]);
    const name = data[i]["index"];
    let element = null;
    let encoderElement = null;
    let normalizerElement = null;
    if (data[i]["total_missing"] > 0) {
      let menu = dtypes.includes(data[i]["dtypes"])
        ? menu1(i, data[i]["index"])
        : menu2(i, data[i]["index"]);

      element = (
        <div >
          <Dropdown key={i} overlay={menu} trigger={["click"]} >
            <a
              className="ant-dropdown-link"
              style={{ color: "salmon" }}
              onClick={(e) => e.preventDefault()}
              href="#"
            >
              {data[i]["total_missing"]} <DownOutlined />
            </a>
          </Dropdown>
          <span style={{display:"inline-block !important"}}>
            {labels(name)}
          </span>
        </div>
      );

    } else {
      element = (
        <a className="ant-dropdown-link" onClick={(e) => e.preventDefault()}>
          {data[i]["total_missing"]}
        </a>
      );
    }


    if(dtypes.includes(data[i]["dtypes"]))
      {
      
     
        if(normalizer)
        {
        
        const defaultValue = (normalizer.hasOwnProperty(name)?normalizer[name]:"None");
       
       
        normalizerElement =  (

          
          <Select
            value={defaultValue}
            style={{ width: "125px", textAlign: "right" }}
            bordered={false}
            onChange={(e) => handelNormalizerChange(e, name)}
          >
            <Option value="max">Max Normalizer</Option>
            <Option value="min">Min Normalizer</Option>
            <Option value="median">Median Normalizer</Option>
            <Option value="mode">Mode Normalizer</Option>
            <Option value="mean">Mean Normalizer</Option>
          </Select>
       

        );
        }
      }else
      {

        
        const defaultValue =  (encoder.hasOwnProperty(name)?encoder[name]:"None");
        encoderElement = (
          <Select
            value={defaultValue}
            style={{ width: "125px", textAlign: "right" }}
            bordered={false}
            onChange={(event) => handleEncoderChange(event, name)}
          >
            <OptGroup
              label={
                <p>
                  Unique Count :{" "}
                  <span style={{ color: "#40a9ff" }}>
                    {data[i]["unique_count"]}
                  </span>
                </p>
              }
            >
              <Option value="one_hot">One Hot Encoder</Option>console.log(value)
              <Option value="label">Label Encoder</Option>
              <Option value="ordinal">Ordinal Encoder</Option>
            </OptGroup>
          </Select>
        )





      }

    rowData.push([
      <TableRow
        hover
        onClick={(event) => handleClick(event, name)}
        role="checkbox"
        aria-checked={isItemSelected}
        tabIndex={-1}
        key={data[i]["index"]}
        selected={isItemSelected}
      >
        <TableCell padding="checkbox">
          <Checkbox
            checked={isItemSelected}
            inputProps={{ "aria-labelledby": i }}
          />
        </TableCell>
        <TableCell key="index" component="th" scope="row" padding="none">
          {data[i]["index"]}
        </TableCell>

        <TableCell key="dtypes" component="th" scope="row">
          {data[i]["dtypes"]}
        </TableCell>

        <TableCell key="total_missing" component="th" scope="row" style={{maxWidth:"150px"}}>
          {element}
        </TableCell>

        <TableCell key="encoder" component="th" scope="row" >
          {encoderElement}
        </TableCell>

        <TableCell key="normalizer" component="th" scope="row">
          {normalizerElement}
        </TableCell>
        </TableRow>
        ,
    ]);
    {
      /*<p>< }</p>  */
    }
  }

  const sendData = () => {
    axios
      .post("http://127.0.0.1:8000/api/processedmetadata", {
        selected: selected,
        action: action,
        encoder: encoder,
        normalizer: normalizer,
        id: sessionStorage.getItem("file_name"),
      })
      .then((res) => {});
  };

  return (
    <div>
      <div className={classes.root}>
        <Paper className={classes.paper}>
          <EnhancedTableToolbar numSelected={selected.length} />
          <TableContainer>
            <Table className={classes.table}>
              <EnhancedTableHead
                classes={classes}
                numSelected={selected.length}
                onSelectAllClick={handleSelectAllClick}
                rowCount={data.length}
              />
              <TableBody>
                {Object.values(rowData).map((value) => {
                  return value;
                })}
              </TableBody>
            </Table>
          </TableContainer>
        </Paper>
      </div>
      <Button onClick={sendData}>Check</Button>
    </div>
  );
}

/*else {
      rowData.push([
        <TableRow
          hover
          onClick={(event) => handleClick(event, name)}
          role="checkbox"
          aria-checked={isItemSelected}
          tabIndex={-1}
          key={data[i]["index"]}
          selected={isItemSelected}
        >
          <TableCell padding="checkbox">
            <Checkbox
              checked={isItemSelected}
              inputProps={{ "aria-labelledby": i }}
            />
          </TableCell>

          <TableCell component="th" id={i} scope="row" padding="none">
            {data[i]["index"]}
          </TableCell>

          <TableCell component="th" scope="row">
            {data[i]["dtypes"]}
          </TableCell>

          <TableCell component="th" scope="row">
            <a
              className="ant-dropdown-link"
              onClick={(e) => e.preventDefault()}
            >
              {data[i]["total_missing"]}
            </a>
          </TableCell>
        </TableRow>,
      ]);
    }
    */
