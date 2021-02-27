import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import '../styles/App.scss';


import About from "./About.jsx";
import Home from "./Home.jsx";

const App = () => {

  return (
    <React.Fragment>
        <h1>Re<span className="accent">q</span>Lock</h1>
        <Router>
          <nav>
              <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
              </ul>
          </nav>
          <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
        </Switch>
        </Router>
    </React.Fragment>
  );
};

export default App;
