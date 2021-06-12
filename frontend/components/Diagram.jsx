import React from "react";
import Diagram, { createSchema, useSchema } from "beautiful-react-diagrams";

const testSchema = {
  nodes: [
    {
      id: "1",
      content: "asdasd",
      coordinates: [100, 100],
    },
    {
      id: "2",
      content: "asasd",
      coordinates: [100, 100],
    },
  ],
};

export const UncontrolledDiagram = (props) => {
  const initialSchema = props.initialSchema;
  if (initialSchema) {
    const currentSchema = createSchema(initialSchema);
    const verifySchema = createSchema(testSchema);
    console.log(currentSchema == verifySchema, currentSchema, verifySchema);

    const [schema, { onChange }] = useSchema(currentSchema);
    return (
      <div style={{ height: "22.5rem" }}>
        <Diagram schema={schema} onChange={onChange} />
      </div>
    );
  }
  return null;
};
