import React, { useEffect } from "react"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import "../styles/App.scss"
import "beautiful-react-diagrams/styles.css"
import { Home } from "./Home.jsx"
import { SignIn } from "./SignIn.jsx"
import { SignUp } from "./SignUp.jsx"
import { LogOut } from "./LogOut.jsx"
import { Projects } from "./Projects.jsx"
import { Navigation } from "./Navigation.jsx"
import { DismissableAlert } from "./DismissableAlert.jsx"
import { AppContext, AppContextProvider } from "./AppContext.jsx"
import { Loader } from "./Loader.jsx"

export const App = () => (
  <AppContextProvider>
    <Router>
      <Loader>
        <Navigation />
        <DismissableAlert />
        <Switch>
          <Route exact path="/">
            <Home />
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
      </Loader>
    </Router>
  </AppContextProvider>
)
