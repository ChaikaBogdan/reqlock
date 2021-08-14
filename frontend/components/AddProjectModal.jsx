import React from "react"
import { useSelector, useDispatch } from "react-redux"
import { HIDE } from "../modal.js"
import { Button, Modal, Form, Col, InputGroup } from "react-bootstrap"
import { addProject } from "../actions.js"
import { useFormik } from "formik"
import * as yup from "yup"

export const AddProjectModal = () => {
  const show = useSelector((state) => state.modal.show)
  const { auth } = useSelector((state) => state.auth)
  const { token } = auth
  const dispatch = useDispatch()
  const handleClose = () => dispatch(HIDE())

  const validationSchema = yup.object().shape({
    name: yup.string("Enter project name").required("Name is required"),
  })

  const formik = useFormik({
    initialValues: {
      name: "",
    },
    validationSchema,
    onSubmit: (values, { setErrors }) =>
      dispatch(addProject(values, token, setErrors, location, history)),
  })

  if (show) {
    return (
      <Modal
        container={document.getElementById("modal-root")}
        show={show}
        onHide={handleClose}
      >
        <Form noValidate onSubmit={formik.handleSubmit}>
          <Modal.Header>
            <Modal.Title>New Project</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form.Row>
              <Form.Group as={Col} md="12">
                <Form.Label>Name</Form.Label>
                <InputGroup hasValidation>
                  <Form.Control
                    type="text"
                    id="name"
                    controlid="name"
                    placeholder="Your project name"
                    value={formik.values.name}
                    onChange={formik.handleChange}
                    isValid={!formik.errors.name}
                    isInvalid={formik.errors.name}
                  />
                  {formik.errors.name && (
                    <Form.Control.Feedback type="invalid">
                      {formik.errors.name}
                    </Form.Control.Feedback>
                  )}
                </InputGroup>
              </Form.Group>
            </Form.Row>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Cancel
            </Button>
            <Button variant="primary" type="submit">
              Add project
            </Button>
          </Modal.Footer>
        </Form>
      </Modal>
    )
  }
  return null
}
