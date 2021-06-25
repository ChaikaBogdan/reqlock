import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "../styles/App.scss";
import "beautiful-react-diagrams/styles.css";
import { About } from "./About.jsx";
import { Home } from "./Home.jsx";
import { SignIn } from "./SignIn.jsx";
import { SignUp } from "./SignUp.jsx";
import { LogOut } from "./LogOut.jsx";
import { Projects } from "./Projects.jsx";
import { Navigation } from "./Navigation.jsx";

const App = () => {
  return (
    <React.Fragment>
      <Router>
        <Navigation />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/projects">
            <Projects />
          </Route>
          <Route path="/signin">
            <SignIn />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>
          <Route path="/logout">
            <LogOut />
          </Route>
        </Switch>
      </Router>
    </React.Fragment>
  );
};

export default App;
