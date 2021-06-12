import React from "react";
import Diagram, { createSchema, useSchema } from "beautiful-react-diagrams";

export const UncontrolledDiagram = (props) => {
  const initialSchema = props.initialSchema;
  if (initialSchema) {
    const currentSchema = createSchema(initialSchema);
    const [schema, { onChange }] = useSchema(currentSchema);
    return (
      <div style={{ height: "22.5rem" }}>
        <Diagram schema={schema} onChange={onChange} />
      </div>
    );
  }
  return null;
};
