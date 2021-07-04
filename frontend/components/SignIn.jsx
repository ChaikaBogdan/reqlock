import React, { useEffect, useContext } from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import { Button, Form, InputGroup } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { useLocation } from "react-router"
import { AppContext } from "./AppContext.jsx"
import { login } from "../actions.js"

export const SignIn = () => {
  const [state, dispatch] = useContext(AppContext)
  const location = useLocation()
  const validationSchema = yup.object().shape({
    email: yup
      .string("Enter your email")
      .email("Enter a valid email")
      .required("Email is required"),
    password: yup
      .string("Enter your password")
      .min(4, "Password should be of minimum 8 characters length")
      .required("Password is required"),
  })
  const history = useHistory()
  const formik = useFormik({
    initialValues: {
      email: "user@reqlock.com",
      password: "user123",
    },
    validationSchema,
    onSubmit: (values, { setErrors }) =>
      dispatch(login(values, setErrors, location, history)),
  })
  return (
    <Form noValidate onSubmit={formik.handleSubmit}>
      <Form.Row>
        <Form.Group>
          <Form.Label>Email address</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="email"
              id="email"
              placeholder="Enter your email"
              value={formik.values.email}
              onChange={formik.handleChange}
              isValid={!formik.errors.email}
            />
            <small className="text-danger">{formik.errors.email}</small>
          </InputGroup>
        </Form.Group>
        <Form.Group>
          <Form.Label>Password</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="password"
              id="password"
              placeholder="Enter your password"
              value={formik.values.password}
              onChange={formik.handleChange}
              isValid={!formik.errors.password}
            />
            <small className="text-danger">{formik.errors.password}</small>
          </InputGroup>
        </Form.Group>
      </Form.Row>
      <Button variant="primary" type="submit">
        Sign In
      </Button>
    </Form>
  )
}
