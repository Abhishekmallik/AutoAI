import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
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


const Check = withStyles((theme) => ({
  head: {
        background: theme.palette.common.black,
        position: '-webkit-sticky',
        position: 'sticky',
        zIndex: 5,
  },
  body: {
    position:'sticky',
    top:0
  },
}))(TableCell);


const useStyles = makeStyles({
  table: {
    width:'auto',
  },
});

export default function CustomizedTables(props) {
  const classes = useStyles();

  const data = props.data 

  if(data === undefined || Object.keys(data).length===0)
  {
      return null
  }


  const columns =data["columns"]

  const index = data["index"]

  const value = data["data"]



  let rows = []

  for(var i = 0 ;i<value.length;i++)
  {
      let row = [<StyledTableCell variant="head">{index[i]}</StyledTableCell>]
      for(var j=0;j<value[i].length;j++)
      {
          row.push(<StyledTableCell>{value[i][j]}</StyledTableCell>)
      }
      rows.push(row);
  }

  return (

    <div >
<Typography variant="h6" id="tableTitle">
    {props.title}
 </Typography>
        
        <TableContainer component={Paper} style={{width:"auto"}} >
 

      <Table stickyHeader={true} className={classes.table} aria-label="customized table"    >
        <TableHead>
          <TableRow>
          <Check >
      
          </Check>
          {
                            columns.map((column)=>{
                                return <StyledTableCell>{column}</StyledTableCell>
                        })
          }
          </TableRow>
        </TableHead>
        <TableBody>
                             {Object.values(rows).map((value)=>{
                                return <StyledTableRow>{value}</StyledTableRow>
                             })}
        </TableBody>
      </Table>
    </TableContainer>
    </div>

  );
}

/*     {rows.map((row) => (
            <StyledTableRow hover key={row.name}>
              <StyledTableCell  component="th" scope="row">
                {row.name}
              </StyledTableCell>
              <StyledTableCell align="right">{row.calories}</StyledTableCell>
              <StyledTableCell align="right">{row.fat}</StyledTableCell>
              <StyledTableCell align="right">{row.carbs}</StyledTableCell>
              <StyledTableCell align="right">{row.protein}</StyledTableCell>
            </StyledTableRow>
          ))}

          */