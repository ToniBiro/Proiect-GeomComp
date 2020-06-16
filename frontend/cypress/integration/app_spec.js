describe("The App", () => {
  it("successfully loads", () => {
    cy.visit("/");
  });

  it("adds a new polygon", () => {
    cy.visit("/");
    cy.contains("Add new polygon").click();
    cy.contains("Polygon #2");
  });

  it("deletes a polygon", () => {
    cy.visit("/");
    cy.contains("Polygon #1").contains("Delete").click();
    cy.contains("Polygon #1").should("not.exist");
  });

  it("intersects two polygons", () => {
    cy.visit("/");
    cy.contains("Intersect with current").click();
    cy.contains("Polygon #2");
  });
});
