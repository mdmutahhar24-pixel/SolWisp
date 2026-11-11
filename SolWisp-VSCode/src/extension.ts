
import * as vscode from "vscode";
import * as path from "path";

function quotePowerShell(value: string): string {
    return `'${value.replace(/'/g, "''")}'`;
}

export function activate(context: vscode.ExtensionContext) {

    const runCommand = vscode.commands.registerCommand(
        "solwisp.run",
        async () => {

            const editor = vscode.window.activeTextEditor;

            if (!editor) {
                vscode.window.showErrorMessage(
                    "No active SolWisp file."
                );
                return;
            }

            const document = editor.document;

            if (document.languageId !== "solwisp") {
                vscode.window.showErrorMessage(
                    "The active file is not a SolWisp file."
                );
                return;
            }

            if (document.isDirty) {
                await document.save();
            }

            const filePath = document.uri.fsPath;

            const config = vscode.workspace.getConfiguration("solwisp");

            const pythonPath = config.get<string>(
                "pythonPath",
                "python"
            );

            const workspaceFolder =
                vscode.workspace.getWorkspaceFolder(document.uri);

            const root = workspaceFolder?.uri.fsPath
                ?? path.dirname(filePath);

            const interpreterPath = config.get<string>(
                "interpreterPath",
                "${workspaceFolder}/run.py"
            ).replace("${workspaceFolder}", root);

            const terminal = vscode.window.createTerminal({
                name: "SolWisp",
                cwd: root
            });

            terminal.show();

            terminal.sendText(
                `& ${quotePowerShell(pythonPath)} ` +
                `${quotePowerShell(interpreterPath)} ` +
                `${quotePowerShell(filePath)}`
            );
        }
    );

    context.subscriptions.push(runCommand);
}

export function deactivate() {}
