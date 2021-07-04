import React, { useState, useEffect } from "react"
import Diagram, { createSchema, useSchema } from "beautiful-react-diagrams"

export const UncontrolledDiagram = (props) => {
  const [initialSchema, setInitialSchema] = useState(props.initialSchema)
  useEffect(() => {}, [initialSchema])

  if (initialSchema.nodes && initialSchema.nodes.length) {
    const currentSchema = createSchema(initialSchema)
    const [schema, { onChange }] = useSchema(currentSchema)

    return (
      <div style={{ height: "22.5rem" }}>
        <Diagram schema={schema} onChange={onChange} />
      </div>
    )
  }
  return null
}
