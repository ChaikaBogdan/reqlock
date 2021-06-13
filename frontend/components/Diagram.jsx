import React, { useState, useEffect } from "react";
import Diagram, { createSchema, useSchema } from "beautiful-react-diagrams";

export const UncontrolledDiagram = (props) => {
  const initialSchema = props.initialSchema;

  if (initialSchema.nodes.length) {
    console.log("UncontrolledDiagram reinit of schema");
    const currentSchema = createSchema(initialSchema);
    const [schema, { onChange }] = useSchema(currentSchema);
    console.log("UncontrolledDiagram renders Diagram itself");
    return (
      <div style={{ height: "22.5rem" }}>
        <Diagram schema={schema} onChange={onChange} />
      </div>
    );
  }
  return null;
};
