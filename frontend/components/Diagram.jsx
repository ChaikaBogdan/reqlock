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

function getObjectDiff(obj1, obj2) {
  const diff = Object.keys(obj1).reduce((result, key) => {
    if (!obj2.hasOwnProperty(key)) {
      result.push(key);
    } else if (obj1[key] === obj2[key]) {
      const resultKeyIndex = result.indexOf(key);
      result.splice(resultKeyIndex, 1);
    }
    return result;
  }, Object.keys(obj2));

  return diff;
}

export const UncontrolledDiagram = (props) => {
  const initialSchema = props.initialSchema;
  if (initialSchema) {
    const currentSchema = createSchema(initialSchema);
    const verifySchema = createSchema(testSchema);

    console.log("DIFF", getObjectDiff(currentSchema, verifySchema));
    console.log(currentSchema, verifySchema);

    const [schema, { onChange }] = useSchema(currentSchema);
    return (
      <div style={{ height: "22.5rem" }}>
        <Diagram schema={schema} onChange={onChange} />
      </div>
    );
  }
  return null;
};
