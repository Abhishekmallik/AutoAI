import React ,{Component} from 'react'
import './App.css';
import {connect} from 'react-redux'
import * as actions from './store/actions/auth'
import Routes from './routes'

class App extends Component{


  componentDidMount(){
    //this.props.onTryAutoSignup();
    
  }


  render(){

    return (
     <Routes></Routes>
    )
  }


}






export default App;
/*

const mapStateToProps = state =>{
  return {
    isAuthenticated : state.token !== null
  }

}


const mapDispatchToProps = dispatch =>{

  return {
    onTryAutoSignup :() =>dispatch(actions.authCheckState())
  }
}


export default connect(mapStateToProps,mapDispatchToProps)(App);

*/









   /*
    state = {
      head :[],
      describe :[],
      missing :[],
      hist :''
    }
    componentDidMount()
    {
      axios.get('http://127.0.0.1:8000/api/datasethead')
      .then(res=>{
        this.setState({
          head:res.data
        })

      })

      axios.get('http://127.0.0.1:8000/api/datasetdescribe')
      .then(res=>{
        this.setState({
          describe:res.data
        })

      })

      axios.get('http://127.0.0.1:8000/api/datasetmissing')
      .then(res=>{
        this.setState({
          missing:res.data
        })

      })

      axios.get('http://127.0.0.1:8000/api/image')
      .then(res=>{
        this.setState({
          hist:res.data['image']
        })
        console.log(res.data)
      })

    
    }
    render(){


      /*
    
      return (
        <div className="App">
          <CustomLayout>
            <Table title = "Head" data = {this.state.head}></Table>
            <TabelComponet title = "Describe" data = {this.state.describe}></TabelComponet>
            <TabelComponet title = "Missing" data = {this.state.missing}></TabelComponet>

            <img src={'data:image/png;base64,'+this.state.hist} alt=""></img>
          </CustomLayout>
        </div>
      );

      


    }
    */



    /*

  function App() {
    return (
      <div className="App">
        <CustomLayout>
          Check
        </CustomLayout>
      </div>
    );
  }
  */