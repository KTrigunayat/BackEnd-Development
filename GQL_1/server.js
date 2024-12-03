const { ApolloServer } = require('apollo-server');
const typeDefs = require('./schema1'); // Import the combined schema
const resolvers = require('./resolvers1'); // Import the combined resolvers

// Create the Apollo Server instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server and listen on the default port
server.listen().then(({ url }) => {
    console.log(`Server ready at ${url}`);
});