import React from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import { Button, Form, Col, InputGroup } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { register } from "../actions.js"
import { useDispatch } from "react-redux"

export const SignUp = () => {
  const dispatch = useDispatch()
  const validationSchema = yup.object().shape({
    email: yup
      .string("Enter your email")
      .email("Enter a valid email")
      .required("Email is required"),
    password1: yup
      .string("Enter your password")
      .min(4, "Password should be of minimum 8 characters length")
      .required("Password is required"),
    password2: yup
      .string("Verify your password")
      .min(4, "Password should be of minimum 8 characters length")
      .required("Password is required"),
  })
  const history = useHistory()
  const formik = useFormik({
    initialValues: {
      email: "user@reqlock.com",
      password1: "user123",
      password2: "user123",
    },
    validationSchema,
    onSubmit: (values, { setErrors }) =>
      dispatch(register(values, setErrors, history)),
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
              controlid="email"
              placeholder="Enter your email"
              value={formik.values.email}
              onChange={formik.handleChange}
              isValid={!formik.errors.email}
              isInvalid={formik.errors.email}
            />
            {formik.errors.email && (
              <Form.Control.Feedback type="invalid">
                {formik.errors.email}
              </Form.Control.Feedback>
            )}
          </InputGroup>
        </Form.Group>
        <Form.Group as={Col} md="4">
          <Form.Label>Password</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="password"
              id="password1"
              controlid="password1"
              placeholder="Enter your password"
              value={formik.values.password1}
              onChange={formik.handleChange}
              isValid={!formik.errors.password1}
              isInvalid={formik.errors.password1}
            />
            {formik.errors.password1 && (
              <Form.Control.Feedback type="invalid">
                {formik.errors.password1}
              </Form.Control.Feedback>
            )}
          </InputGroup>
        </Form.Group>
        <Form.Group as={Col} md="4">
          <Form.Label>Password confirmation</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type="password"
              id="password2"
              controlid="password2"
              placeholder="Confrim your password"
              value={formik.values.password2}
              onChange={formik.handleChange}
              isValid={!formik.errors.password2}
              isInvalid={formik.errors.password2}
            />
            {formik.errors.password2 && (
              <Form.Control.Feedback type="invalid">
                {formik.errors.password2}
              </Form.Control.Feedback>
            )}
          </InputGroup>
        </Form.Group>
      </Form.Row>
      <Button variant="primary" type="submit">
        Sign Up
      </Button>
    </Form>
  )
}
