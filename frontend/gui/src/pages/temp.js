import React,{Component} from 'react'
import CustomLayout from '../containers/Layout'
import Table from '../containers/TempTable'
import axios from 'axios'

class Processing extends Component{


  state = {
    dtypes :[],
        actions :{},
        columns :[],
        encodet :{},
        normalizer :{}
  }
  componentDidMount()
  {
    let params = {
      id :sessionStorage.getItem('file_name')
    }


    

    axios.get('http://127.0.0.1:8000/api/csvmetadata',{params:params})
    .then(res=>{
      this.setState({
        dtypes:res.data
      })
      console.log(res.data)
    })
   
    axios.get('http://127.0.0.1:8000/api/processedmetadata',{params:params})
        .then(res=>{
          this.setState({
            columns :res.data['columns'],
            actions :res.data['actions'],
            encoder :res.data['encoder'],
            normalizer :res.data['normalizer']
          })
        })
}


render(){

return (
    <div className="App">
      <CustomLayout  k="3">
        <Table data={this.state.dtypes} columns={this.state.columns} actions ={this.state.actions} encoder={this.state.encoder} normalizer={this.state.normalizer}  title="Data Types"></Table>
      </CustomLayout>
    </div>
  );
}

}
export default  Processing;