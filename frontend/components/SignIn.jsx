import React from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import { Button, Form, Col, InputGroup } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { useLocation } from "react-router"
import { login } from "../actions.js"
import { useDispatch } from "react-redux"

export const SignIn = () => {
  const dispatch = useDispatch()
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
        <Form.Group as={Col} md="4">
          <Form.Label>Email address</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="email"
              id="email"
              controlId="email"
              placeholder="Enter your email"
              value={formik.values.email}
              onChange={formik.handleChange}
              isValid={!formik.errors.email}
              isInvalid={formik.errors.email}
            />
            {formik.errors.email && <Form.Control.Feedback type="invalid">{formik.errors.email}</Form.Control.Feedback>}
          </InputGroup>
        </Form.Group>
        <Form.Group as={Col} md="4">
          <Form.Label>Password</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="password"
              id="password"
              controlId="password"
              placeholder="Enter your password"
              value={formik.values.password}
              onChange={formik.handleChange}
              isValid={!formik.errors.password}
              isInvalid={formik.errors.password}
            />
            {formik.errors.password && <Form.Control.Feedback type="invalid">{formik.errors.password}</Form.Control.Feedback>}
          </InputGroup>
        </Form.Group>
      </Form.Row>
      <Button variant="primary" type="submit">
        Sign In
      </Button>
    </Form>
  )
}
