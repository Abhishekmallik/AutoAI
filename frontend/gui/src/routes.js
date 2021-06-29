import React from "react";
import DatasetInfo from "./pages/datasetinfo";
import Plots from "./pages/plots";
import Processing from "./pages/process";
import Temp from "./pages/temp";
import Model from "./pages/model";
import Login from "./pages/login";
import Home from "./pages/dashboard";
import Files from "./pages/file"
import Result from "./pages/allresult"
import HomePage from "./pages/homepage"
import NewLogin from "./pages/newlogin"
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { createBrowserHistory } from 'history';

export const history = createBrowserHistory();

const BaseRouter = () => {
  return (
    <Router history={history}>
     
      <Switch>
     
        <Route
          path="/datasetinfo"
          render={(props) => <DatasetInfo {...props} isAuthed={true} />}
        ></Route>
        <Route path="/plots" component={Plots}></Route>

        <Route path="/process" component={Temp}></Route>

        <Route path="/model" component={Model}></Route>

        <Route path="/files" component={Files}></Route>

        <Route path="/result" component={Result}></Route>
        <Route path="/home" component={Home}></Route>
        <Route path="/working" component={NewLogin}></Route>
        <Route path="/login" component={Login}></Route>
        <Route path="/" component={HomePage}></Route>

        
        


        

      </Switch>
    </Router>
  
  );
};

export default BaseRouter;
