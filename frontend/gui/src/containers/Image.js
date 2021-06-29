import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

export default function FullWidthGrid(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      
      
      
      <Grid container spacing={3}>
   
        <Grid item xs={12} sm={6}>
           
            <Paper className={classes.paper}>
                <Typography variant="h4" id="tableTitle" style={{fontWeight:'10'}}>
                    Plot
                </Typography> 
                <img style={{ maxWidth: "100%",maxHeight: "100%"}}src={props.src1} width="750"></img>
            </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
           
            <Paper className={classes.paper}>
            <Typography variant="h4" id="tableTitle" style={{fontWeight:'10'}}>
                    Plot
                </Typography>
                <img style={{ maxWidth: "100%",maxHeight: "100%"}} src={props.src2} width="750"></img>
            </Paper>
        </Grid>
       
      </Grid>
    </div>
  );
}


