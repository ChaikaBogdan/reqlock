import React from "react"
import { Navbar, Nav, NavDropdown } from "react-bootstrap"
import { LinkContainer } from "react-router-bootstrap"
import { useSelector } from "react-redux"

export const Navigation = () => {
  const { auth } = useSelector((state) => state.auth)
  const { token, username } = auth
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
          {token && (
            <LinkContainer to="/projects">
              <Nav.Link>Projects</Nav.Link>
            </LinkContainer>
          )}
          {!token && (
            <>
              <LinkContainer to="/signup">
                <Nav.Link>Sign Up</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/signin">
                <Nav.Link>Sign In</Nav.Link>
              </LinkContainer>
            </>
          )}
        </Nav>
        {token && username && (
          <>
            <NavDropdown title={username} id="basic-nav-dropdown">
              <LinkContainer to="/logout">
                <NavDropdown.Item>Log out</NavDropdown.Item>
              </LinkContainer>
            </NavDropdown>
          </>
        )}
      </Navbar.Collapse>
    </Navbar>
  )
}
