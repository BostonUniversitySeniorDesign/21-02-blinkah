import React from "react";
import { Component } from 'react'
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";
import Search from "@material-ui/icons/Search";
import CustomInput from "components/CustomInput/CustomInput.js";
import Button from "components/CustomButtons/Button.js";
import axios from 'axios';

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
var tableDataValues = [[]]
var licensePlate = ""

export default function TableList() {
  function handleData() {
    var x = document.getElementById("input1").value
    console.log(x)
    var y = "http://161.35.50.175:8000/reports/license_plate/"
    var z = y.concat(x)
    var z = z.concat("/")
    axios
      .get(z)
      .then((res) => {
        console.log("response from main API: ", res);
        console.log("Data from API: ", res.data);
        const resData = res.data;
        console.log("test")
        console.log(resData[0].license_plate)
        tableDataValues=[
          [resData[0].id, resData[0].latitude, resData[0].longitude, resData[0].infraction, resData[0].timestamp]
        ]
        licensePlate = resData[0].license_plate;
        console.log(tableDataValues)
        var container = document.getElementById("license");
        window.location.href="#";
      })
      .catch((err) => {
        console.log(err);
      })
  };
  const classes = useStyles();
  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={12}>
      <div className={classes.searchWrapper}>
        <CustomInput id="input1"
          formControlProps={{
            className: classes.margin + " " + classes.search
          }}
          inputProps={{
            placeholder: "License Plate Search",
            inputProps: {
              "aria-label": "Search"
            }
          }}
        />
        <Button onClick={ () => handleData()} color="white" aria-label="edit" justIcon round>
          <Search />
        </Button>
      </div>

        <Card>
          <CardHeader color="primary">
            <h4 className={classes.cardTitleWhite}>License Plate: {licensePlate}</h4>
            <p className={classes.cardCategoryWhite}>
               <br />
              List of infractions
            </p>
          </CardHeader>
          <CardBody>
            <Table id="license"
              tableHeaderColor="primary"
              tableHead={["Report ID", "Latitude", "Longitude", "Infraction", "Date"]}
              tableData={tableDataValues}
            />
          </CardBody>
        </Card>
      </GridItem>
    </GridContainer>
  );
}
  // fetch('http://161.35.50.175:8000/reports/license_plate/BC18351/')
  // .then(response => response.json())
  // .then(data => console.log(data));
  // tableDataValues=[
  //        [resData[0].id, resData[0].latitude, resData[0].longitude, resData[0].infraction, resData[0].timestamp]
  //    