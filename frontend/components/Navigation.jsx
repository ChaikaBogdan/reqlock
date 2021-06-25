import React from "react";
import {
  Navbar,
  Nav,
  NavDropdown,
  Form,
  FormControl,
  Button,
} from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export const Navigation = () => {
  return (
    <Navbar bg="light" expand="lg">
      <LinkContainer to="/">
        <Navbar.Brand to="/">
          Re<span className="accent">q</span>Lock
        </Navbar.Brand>
      </LinkContainer>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <LinkContainer to="/projects">
            <Nav.Link>Projects</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/about">
            <Nav.Link>About</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/signup">
            <Nav.Link>Sign Up</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/signin">
            <Nav.Link>Sign In</Nav.Link>
          </LinkContainer>
        </Nav>
        <NavDropdown title="John Doe" id="basic-nav-dropdown">
          <LinkContainer to="/preferences">
            <NavDropdown.Item>Preferences</NavDropdown.Item>
          </LinkContainer>
          <NavDropdown.Divider />
          <LinkContainer to="/logout">
            <NavDropdown.Item>Log out</NavDropdown.Item>
          </LinkContainer>
        </NavDropdown>
      </Navbar.Collapse>
    </Navbar>
  );
};
