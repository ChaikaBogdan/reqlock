import React from "react";
import { Navbar, Nav, NavDropdown } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

const Navigation = () => {
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
        </Nav>

        <NavDropdown title="User" className="navigation-dropdwon" id="basic-nav-dropdown">
          <NavDropdown.Item>Preferences</NavDropdown.Item>
          <LinkContainer to="/about">
            <NavDropdown.Item>About</NavDropdown.Item>
          </LinkContainer>
          <NavDropdown.Divider />
          <NavDropdown.Item>Log out</NavDropdown.Item>
        </NavDropdown>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Navigation;
