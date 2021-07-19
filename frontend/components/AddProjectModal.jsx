import React from "react"
import { useSelector, useDispatch } from "react-redux"
import { HIDE } from "../modal.js"
import Portal from "react-overlays/Portal"
import { useHistory } from "react-router-dom"
import { Formik, Form, Field, ErrorMessage } from "formik"
import { Button, Modal, Col, InputGroup } from "react-bootstrap"
import { useFormik } from "formik"
import * as yup from "yup"

export const AddProjectModal = () => {
  const show = useSelector((state) => state.modal.show)
  const dispatch = useDispatch()
  const handleClose = () => dispatch(HIDE())

  const validationSchema = yup.object().shape({
    name: yup.string("Enter project name").required("Name is required"),
  })

  const formik = useFormik({
    initialValues: {
      name: "John Doe Project",
    },
    validationSchema,
    onSubmit: (values, {}) => dispatch(),
  })
  if (show) {
    return (
      // SHIT DOES NOT WORK
      <Portal container={document.getElementById("modal-root")}>
        <Modal show={show} onHide={handleClose}>
          <Form noValidate onSubmit={formik.handleSubmit}>
            <Modal.Header>
              <Modal.Title>Add project</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form.Row>
                <Form.Group as={Col} md="4">
                  <Form.Label>Project name</Form.Label>
                  <InputGroup hasValidation>
                    <Form.Control
                      type="name"
                      id="name"
                      controlid="name"
                      placeholder="Your project name"
                      value={formik.values.email}
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
      </Portal>

      // SHIT WORKS
      // <>
      //   <Modal show={show} onHide={handleClose}>
      //     <Modal.Header closeButton>
      //       <Modal.Title>Modal heading</Modal.Title>
      //     </Modal.Header>
      //     <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
      //     <Modal.Footer>
      //       <Button variant="secondary" onClick={handleClose}>
      //         Close
      //       </Button>
      //       <Button variant="primary" onClick={handleClose}>
      //         Save Changes
      //       </Button>
      //     </Modal.Footer>
      //   </Modal>
      // </>
    )
  }
  return null
}
