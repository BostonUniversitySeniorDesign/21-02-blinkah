import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";

const styles = {
  cardCategoryWhite: {
    "&,& a,& a:hover,& a:focus": {
      color: "rgba(255,255,255,.62)",
      margin: "0",
      fontSize: "14px",
      marginTop: "0",
      marginBottom: "0"
    },
    "& a,& a:hover,& a:focus": {
      color: "#FFFFFF"
    }
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none",
    "& small": {
      color: "#777",
      fontSize: "65%",
      fontWeight: "400",
      lineHeight: "1"
    }
  }
};

const useStyles = makeStyles(styles);

export default function TableList() {
  const classes = useStyles();
  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={12}>
        <Card>
          <CardHeader color="primary">
            <h4 className={classes.cardTitleWhite}>License Plate: FXZ2038</h4>
            <p className={classes.cardCategoryWhite}>
              White 2003 Honda Accord <br />
              List of infractions

            </p>
          </CardHeader>
          <CardBody>
            <Table
              tableHeaderColor="primary"
              tableHead={["Report ID", "City", "Action", "Report Entity", "Date"]}
              tableData={[
                ["1543", "Boston", "Ran Red Light", "Allstate", "03/08/2020"],
                ["1876", "Brookline", "Speeding", "Allstate", "05/23/2020"],
                ["1943", "Brighton", "Speeding", "Allstate", "06/01/2020"],
                ["2054", "Boston, South", "Swerving", "Emergency Services", "07/04/2020"],
                ["2098", "Newton", "Outdated Registration", "MA RMV", "09/18/2020"],
                ["2256", "Boston", "Ran Stop Sign", "Allstate", "11/15/2020"]
              ]}
            />
          </CardBody>
        </Card>
      </GridItem>
    </GridContainer>
  );
}
