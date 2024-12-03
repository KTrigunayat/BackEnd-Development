const mockusers = [
    { id: 1, name: "Alice", email:"foo@bar.com"},
    { id: 2, name: "Bob", email:"baz@qux.com"},

];


const resolvers = {
    Query: {
        user: (_, {id}) => mockusers.find(user => user.id === Number(id))
    }
};

module.exports = resolvers;
