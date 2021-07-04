import React, { useEffect, useContext } from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import { Button, Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { AppContext } from "./AppContext.jsx"
import { register } from "../actions.js"

export const SignUp = () => {
  const [state, dispatch] = useContext(AppContext)
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
      <Form.Group>
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          id="email"
          placeholder="Enter your email"
          value={formik.values.email}
          onChange={formik.handleChange}
          isValid={!formik.errors.email}
        />
        <small className="text-danger">{formik.errors.email}</small>
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          id="password1"
          placeholder="Enter your password"
          value={formik.values.password1}
          onChange={formik.handleChange}
          isValid={!formik.errors.password1}
        />
        <small className="text-danger">{formik.errors.password1}</small>
        <Form.Label>Password confrimation</Form.Label>
        <Form.Control
          type="password"
          id="password2"
          placeholder="Confrim your password"
          value={formik.values.password2}
          onChange={formik.handleChange}
          isValid={!formik.errors.password2}
        />
        <small className="text-danger">{formik.errors.password2}</small>
      </Form.Group>
      <Button variant="primary" type="submit">
        Sign Up
      </Button>
    </Form>
  )
}
