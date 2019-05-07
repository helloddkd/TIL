const getUser = id => {
    const users = [
        { id: 1, githubID: 'eduyu' },
        { id: 2, githubID: 'edujohn' },
    ];
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            const user = users.find(user => user.id === id);
            if (user) {
                resolve(user);
            } else {
                reject(new Error(`No Such user with id ${id}`));
            }
        }, 2000)
    })
};

const getRepos = user => {
    const repos = [
        'TIL',
        'Workshop_HW',
        'Python',
        'JS'
    ];
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if (repos) {
                resolve(repos);
            } else {
                reject(new Error('cannot find the repo and commits'));
            }
        }, 2000)
    })

};

const getCommits = repo => {
    const commits = [
        'Init repo',
        'Make index.html'
    ];
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERRRRORRRR'));
            }
        }, 2000)
    });
};


async function main () {
    try {
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length);
    } catch (e) {
        console.error(e);
    }

};

main();


// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])