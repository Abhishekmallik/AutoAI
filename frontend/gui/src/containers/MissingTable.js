import React ,{useState} from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import { Menu, Dropdown } from 'antd';
import { DownOutlined } from '@ant-design/icons';
import { Tag, Divider } from 'antd';
import Checkbox from '@material-ui/core/Checkbox';


const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.white,
    color: theme.palette.common.black,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);



const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);


const useStyles = makeStyles({
  table: {

  },
});

export default function CustomizedTables(props) {
    const classes = useStyles();
    const data  = props.data;
    console.log(data)
    const [TagState,setTagState] = useState({

      'tags': new Array(data.length)

    }) 


    if(Object.keys(data).length===0)
    {
        return null 
    }


    
   
     const handleMenuClick = e => {
      console.log('Hi')
      let obj  = e.key
      obj = JSON.parse(obj)
 


      let newTageState = new Array(data.length)
      TagState.tags[obj.id]= <Tag color={obj.color} style={{marginLeft:'7px'}}>{obj['message']}</Tag>
 
      setTagState({

        'tags': TagState.tags
      })
    };

    const keys = Object.keys(data[0])
    
    function menu1(index){
        return (<Menu onClick={handleMenuClick}>
          <Menu.Item key = {'{ "id":'+index+', "message":"Replaced with mean","color":"success"}'}>
                Replace with mean
          </Menu.Item>
          <Menu.Item key = {'{ "id":'+index+', "message":"Replaced with median","color":"success"}'}>
                Replace with median
          </Menu.Item>
          <Menu.Item key = {'{ "id":'+index+', "message":"Replaced with mode","color":"success"}'}>
                Replace with mode
          </Menu.Item >
          <Menu.Item danger key = {'{ "id":'+index+', "message":"Delete Missing Records","color":"error"}' }>Delete Missing Records</Menu.Item>
          <Menu.Item danger key = {'{ "id":'+index+', "message":"Delete Column","color":"error"}'} >Delete Column</Menu.Item>
        </Menu>)
    };

      function menu2(index){
        return ( 
        <Menu onClick={handleMenuClick}>
          <Menu.Item key = {'{ "id":'+index+', "message":"Replace with minimum frequency","color":"success"}'}>
                Replace with minimum frequency
          </Menu.Item>
          <Menu.Item key = {'{ "id":'+index+', "message":"Replace with maximum frequency","color":"success"}'}>
                 Replace with maximum frequency
          </Menu.Item>
          <Menu.Item danger  key = {'{ "id":'+index+', "message":"Deleted Missing Records","color":"error"}' }>Delete Missing Records
          </Menu.Item>
          <Menu.Item danger  key = {'{ "id":'+index+', "message":"Delete Column","color":"error"}' }>Delete Column</Menu.Item>
        </Menu>
      )};



 
      // dtypes = ['int64','float64','decimal'];
    

      let rowData = []
      
      const dtypes = ['int64','float64','decimal']
      


      for(var i = 0;i<data.length;i++)
      {
            if(data[i]['total_missing']>0)
            {

                let element = ''

                if(data[i]['dtypes'] ==='float64')
                {
                    
                    element =  <div><Dropdown key = {i} overlay={menu1(i)} trigger={["click"]}>
               
                    <a className="ant-dropdown-link" style={{color:'salmon'}} onClick={e => e.preventDefault()} href="#">
                    {data[i]['total_missing']} <DownOutlined />
                   
                    </a>
                    
                  </Dropdown>
                  <span style={{width:'50px', display: 'inline-block'}}>
                  {TagState.tags[i]}  
                  </span>

                  </div>


                }else{
               
                    element =  <div><Dropdown  overlay={menu2(i)} trigger={["click"]}>
                      
                  <a className="ant-dropdown-link" style={{color:'salmon'}} onClick={e => e.preventDefault()} href="#">
                  {data[i]['total_missing']} <DownOutlined />
                  </a>
                 
                  </Dropdown>
                  <span style={{width:'50px', display: 'inline-block'}}>
                  {TagState.tags[i]}  
                  </span>

                  </div>
                }




                rowData.push([
                <StyledTableRow>

                    <StyledTableCell>
                      <Checkbox
                          
                          />
                    </StyledTableCell>
                    <StyledTableCell  component="th" scope="row">
                        {data[i]['index']}
                    </StyledTableCell>

                    <StyledTableCell  component="th" scope="row">
                        {data[i]['dtypes']}
                    </StyledTableCell>

                    <StyledTableCell  component="th" scope="row">
                        {element}
                        
                    </StyledTableCell>
                    
                </StyledTableRow>])

            }else
            {
                rowData.push([
                <StyledTableRow>
                    
                    <StyledTableCell>
                      <Checkbox
                           
                            
                          />
                    </StyledTableCell>

                    <StyledTableCell  component="th" scope="row">
                        {data[i]['index']}
                    </StyledTableCell>

                    <StyledTableCell  component="th" scope="row">
                        {data[i]['dtypes']}
                    </StyledTableCell>

                    <StyledTableCell  component="th" scope="row">
                        <a className="ant-dropdown-link" onClick={e => e.preventDefault()}>
                          {data[i]['total_missing']}  
                        </a>
                    </StyledTableCell>
                   
                </StyledTableRow>])

            }
      }

     
  return (

    <div>
  <Typography variant="h6" id="tableTitle">
    {props.title}
 </Typography>
        <TableContainer component={Paper}>
 

      <Table className={classes.table} aria-label="customized table">
        <TableHead>

          <TableRow>
                <TableCell padding="checkbox">
                <Checkbox
                 
                  inputProps={{ 'aria-label': 'select all desserts' }}
                />
              </TableCell>
                { 
                    keys.map((key)=>{
                        return (<StyledTableCell>{key}</StyledTableCell>)
                    })   
                }
          </TableRow>
        </TableHead>
        <TableBody>
                            {Object.values(rowData).map((value)=>{
                                return value
                             })}
        </TableBody>
      </Table>
    </TableContainer>
    </div>

  );
}
