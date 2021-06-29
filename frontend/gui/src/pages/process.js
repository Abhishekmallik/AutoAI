import React,{Component} from 'react'
import CustomLayout from '../containers/Layout'
import Table from '../containers/MissingTable'
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



        axios.get('http://127.0.0.1:8000/api/datasettypes')
        .then(res=>{
          this.setState({
            dtypes:res.data
          })
          console.log(res.data)
        })

        let params = {
          id :sessionStorage.getItem('file_name')
        }

        
        axios.get('http://127.0.0.1:8000/api/processedmetadata',{paramas:params})
        .then(res=>{
          console.log(res.data)
          this.setState({
            columns :res.data['columns'],
            actions :res.data['actions'],
            encoder :res.data['encoder'],
            normalizer :res.data['normalizer']
          })
        })

    }
    render(){
      console.log('Times')
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